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
    .appName("gold-dim_host") \
    .config("spark.driver.host", "spark-notebook") \
    .config("spark.driver.bindAddress", "0.0.0.0") \
    .enableHiveSupport() \
    .getOrCreate()


# In[7]:


df_dim_host = spark.sql(
    '''
    WITH recency_ranking_list AS (
    select  
	host_id, 
	host_name, 
	DATE(host_since) as host_since,
	host_location,
	host_is_superhost,
	host_neighbourhood, 
	host_listings_count,
	host_total_listings_count,
	host_verifications,
	host_has_profile_pic,
	host_identity_verified,
	now() as updated_at_utc8,
 ROW_NUMBER() OVER (
            PARTITION BY host_id 
            ORDER BY extraction_date DESC
        ) as recency_rank
from airbnb_silver.stg_listings 
)
SELECT 
    host_id,
    host_name,
    host_since,
    host_location,
    host_is_superhost,
    host_neighbourhood,
    host_listings_count,
    host_verifications,
    host_has_profile_pic,
    host_identity_verified,
    updated_at_utc8
FROM 
    recency_ranking_list
WHERE 
    recency_rank = 1
;
    '''
)


# In[8]:




# In[9]:


ch_url = "jdbc:ch://analytics-clickhouse:8123/airbnb_gold?user=spark_admin&password=spark_123"

ch_properties = {
    "driver": "com.clickhouse.jdbc.ClickHouseDriver",
    "createTableOptions": "ENGINE = MergeTree() ORDER BY (host_id)"
}

print("Attempting write with spark_admin user...")
try:
    df_dim_host.write.jdbc(
        url=ch_url, 
        table="dim_hosts", 
        mode="overwrite", 
        properties=ch_properties
    )
    print("✅ Data loaded into ClickHouse.")
except Exception as e:
    print(f"❌ Error: {e}")

