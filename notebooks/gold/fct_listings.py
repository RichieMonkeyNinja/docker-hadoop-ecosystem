#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pyspark.sql import SparkSession
import os 
import pandas as pd

# This forces Pandas to show every single row and column
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

os.environ['HADOOP_USER_NAME'] = 'root'

spark = SparkSession.builder \
    .appName("gold-fct_listings") \
    .config("spark.driver.host", "spark-notebook") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .enableHiveSupport() \
    .getOrCreate()


# In[28]:


df_fct_listings = spark.sql(
    '''
with ranked_listings as (
	select 
		id,
		host_id,
		extraction_date,
		city,
		price,
		minimum_nights,
		maximum_nights,
		has_availability,
		availability_30,
		availability_60,
		availability_90,
		availability_365,
		number_of_reviews,
		number_of_reviews_l30d,
		number_of_reviews_ltm,
  estimated_occupancy_l365d,
		first_review,
		last_review,
		review_scores_rating,
		review_scores_accuracy,
		review_scores_cleanliness,
		review_scores_checkin,
		review_scores_communication,
		review_scores_location,
		review_scores_value,
		instant_bookable,
		now() as updated_at_utc8,
		ROW_NUMBER() OVER (
            PARTITION BY id 
            ORDER BY extraction_date DESC
        ) as rank_desc
from airbnb_silver.stg_listings 	
)
select 		
		id,
		host_id,
		extraction_date,
		DATE_FORMAT(extraction_date, 'yyyy-MM') as extraction_month,
		city,
		price,
		minimum_nights,
		maximum_nights,
		has_availability,
		availability_30,
		availability_60,
		availability_90,
		availability_365,
		number_of_reviews,
		number_of_reviews_l30d,
		number_of_reviews_ltm,
        estimated_occupancy_l365d,
		first_review,
		last_review,
		review_scores_rating,
		review_scores_accuracy,
		review_scores_cleanliness,
		review_scores_checkin,
		review_scores_communication,
		review_scores_location,
		review_scores_value,
		instant_bookable,
		now() as updated_at_utc8,
		CASE WHEN rank_desc = 1 THEN 1 ELSE 0 END as is_latest 
from ranked_listings
;
    '''
)


# In[29]:




# In[30]:


ch_url = "jdbc:ch://analytics-clickhouse:8123/airbnb_gold?user=spark_admin&password=spark_123"

ch_properties = {
    "driver": "com.clickhouse.jdbc.ClickHouseDriver",
    "createTableOptions": "ENGINE = MergeTree() ORDER BY (id, extraction_date, host_id)"
}

print("Attempting write with spark_admin user...")
try:
    df_fct_listings.write.jdbc(
        url=ch_url, 
        table="fct_listings", 
        mode="overwrite", 
        properties=ch_properties
    )
    print("✅ Data loaded into ClickHouse.")
except Exception as e:
    print(f"❌ Error: {e}")

