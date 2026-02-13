#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
import os 
import pandas as pd

# This forces Pandas to show every single row and column
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

os.environ['HADOOP_USER_NAME'] = 'root'

spark = SparkSession.builder \
    .appName("bronze-spark-upload-hdfs") \
    .config("spark.driver.host", "spark-notebook") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .enableHiveSupport() \
    .getOrCreate()


# In[2]:


df_listings = spark.sql('SELECT * FROM airbnb_bronze.listings')


# In[4]:


# Remove url and metadata columns (such as scraping related information)
df_listings = df_listings.drop('listing_url','host_url','picture_url','scrape_id','last_scraped', 'host_thumbnail_url','host_picture_url')


# In[5]:


# View one row vertically (great for inspection)
# df_listings.describe().show(n=1, vertical=True)

# Convert to Pandas for a beautiful interactive table (if in a Notebook)
# df_listings.describe().toPandas().transpose()


# In[6]:


# Remove columns with only NULL values

df_listings = df_listings.drop('calendar_updated','neighbourhood_group_cleansed')

# Check distinct values of neighbourhood (only NULL or Neighbourhood highlights)
# df_listings.select('neighbourhood').distinct().show()
df_listings = df_listings.drop('neighbourhood')

# Remove columns that does not hold meaningful//analyzable values

df_listings = df_listings.drop('name','description','neighborhood_overview','host_about','license','bathrooms_text','source')


# In[8]:


# some columns has data types that can be formatted

# 1) host_since: string -> datetime
# 2) host_response_time: string -> datetime
# 3） host_response_rate: string -> float
# 4) host_acceptance_rate: string -> float
# 5) price: string -> float
# 6) first_review: string -> datetime
# 7) last_review: string -> datetime

from pyspark.sql.functions import to_timestamp, col, regexp_replace, coalesce, lit, size, current_timestamp

datetime_cols = ['host_since','first_review','last_review']
for c in datetime_cols:
    df_listings = df_listings.withColumn(
        c,
        to_timestamp(c, 'yyyy-MM-dd')
    )

df_listings = df_listings.withColumn(
    'price',
    regexp_replace(col('price'), "[$, ]", "").cast("float")
)

for c in ['host_response_rate','host_acceptance_rate']:
    df_listings = df_listings.withColumn(
        c,
        coalesce(
             regexp_replace(c, "%", "").cast("float") / 100,
            lit(0.0)
        )
    )

# Remove rows where Price is NULL

df_listings = df_listings.filter(
    col('price').isNotNull()
)


# In[10]:


df_listings = df_listings.withColumn('updated_at_utc_0', current_timestamp())


# In[11]:


hdfs_destination = "hdfs://namenode:9000/user/hive/warehouse/airbnb.db/silver/listings"

(df_listings.write
    .mode("overwrite") \
    .partitionBy("extraction_date", "city") \
    .format("parquet") \
    .save(hdfs_destination))

print(f"✅ Ingestion complete. Data stored at: {hdfs_destination}")


# In[14]:


# 1. Create the Database
spark.sql("CREATE DATABASE IF NOT EXISTS airbnb_silver")

# 2. Create the Table
spark.sql('''
CREATE EXTERNAL TABLE IF NOT EXISTS airbnb_silver.stg_listings (
    id BIGINT,

    host_id BIGINT,
    host_name STRING,
    host_since TIMESTAMP,
    host_location STRING,
    host_response_time STRING,
    host_response_rate DOUBLE,
    host_acceptance_rate DOUBLE,
    host_is_superhost STRING,
    host_neighbourhood STRING,
    host_listings_count DOUBLE,
    host_total_listings_count DOUBLE,
    host_verifications STRING,
    host_has_profile_pic STRING,
    host_identity_verified STRING,

    neighbourhood_cleansed STRING,
    latitude DOUBLE,
    longitude DOUBLE,

    property_type STRING,
    room_type STRING,
    accommodates BIGINT,
    bathrooms DOUBLE,
    bedrooms DOUBLE,
    beds DOUBLE,
    amenities STRING,

    price FLOAT,

    minimum_nights BIGINT,
    maximum_nights BIGINT,
    minimum_minimum_nights DOUBLE,
    maximum_minimum_nights DOUBLE,
    minimum_maximum_nights DOUBLE,
    maximum_maximum_nights DOUBLE,
    minimum_nights_avg_ntm DOUBLE,
    maximum_nights_avg_ntm DOUBLE,

    has_availability STRING,
    availability_30 BIGINT,
    availability_60 BIGINT,
    availability_90 BIGINT,
    availability_365 BIGINT,

    calendar_last_scraped STRING,

    number_of_reviews BIGINT,
    number_of_reviews_ltm BIGINT,
    number_of_reviews_l30d BIGINT,
    availability_eoy BIGINT,
    number_of_reviews_ly BIGINT,

    estimated_occupancy_l365d BIGINT,
    estimated_revenue_l365d DOUBLE,

    first_review TIMESTAMP,
    last_review TIMESTAMP,

    review_scores_rating DOUBLE,
    review_scores_accuracy DOUBLE,
    review_scores_cleanliness DOUBLE,
    review_scores_checkin DOUBLE,
    review_scores_communication DOUBLE,
    review_scores_location DOUBLE,
    review_scores_value DOUBLE,

    instant_bookable STRING,

    calculated_host_listings_count BIGINT,
    calculated_host_listings_count_entire_homes BIGINT,
    calculated_host_listings_count_private_rooms BIGINT,
    calculated_host_listings_count_shared_rooms BIGINT,

    reviews_per_month DOUBLE,
          
    updated_at_utc_0 TIMESTAMP
)
PARTITIONED BY (
    extraction_date DATE,
    city STRING
)
STORED AS PARQUET
LOCATION '/user/hive/warehouse/airbnb.db/silver/listings';
''')

# 3. Register the partitions (Crucial!)
spark.sql("MSCK REPAIR TABLE airbnb_silver.stg_listings")

