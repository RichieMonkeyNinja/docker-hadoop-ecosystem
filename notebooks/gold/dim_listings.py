#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pyspark.sql import SparkSession
import os 
import pandas as pd

# This forces Pandas to show every single row and column
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

os.environ['HADOOP_USER_NAME'] = 'root'

spark = SparkSession.builder \
    .appName("gold-dim_listings") \
    .config("spark.driver.host", "spark-notebook") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .enableHiveSupport() \
    .getOrCreate()


# In[4]:


df_dim_listings = spark.sql(
    '''
select distinct 
		id,
		host_id,
		neighbourhood_cleansed,
		latitude,
		longitude,
		property_type,
		room_type,
		accommodates,
		bathrooms,
		bedrooms,
		beds,
		case when amenities like '%wifi%' then 1 else 0 end as provided_wifi,
		case when amenities like '%parking%' then 1 else 0 end as provided_parking,
		amenities as all_amenities
from airbnb_silver.stg_listings  
;
    '''
)


# In[5]:




# In[7]:


ch_url = "jdbc:ch://analytics-clickhouse:8123/airbnb_gold?user=spark_admin&password=spark_123"

ch_properties = {
    "driver": "com.clickhouse.jdbc.ClickHouseDriver",
    "createTableOptions": "ENGINE = MergeTree() ORDER BY (id, host_id)"
}

print("Attempting write with spark_admin user...")
try:
    df_dim_listings.write.jdbc(
        url=ch_url, 
        table="dim_listings", 
        mode="overwrite", 
        properties=ch_properties
    )
    print("✅ Data loaded into ClickHouse.")
except Exception as e:
    print(f"❌ Error: {e}")

