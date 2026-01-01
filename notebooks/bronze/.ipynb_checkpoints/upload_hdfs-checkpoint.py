#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os
import logging
import sys

# ------------------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------------------
os.environ["HADOOP_USER_NAME"] = "root"

# ------------------------------------------------------------------------------
# Logging (stdout so Airflow can capture it)
# ------------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# Spark Session
# ------------------------------------------------------------------------------
logger.info("Starting Spark Bronze Ingestion Job")

spark = (
    SparkSession.builder
    .appName("bronze-spark-upload-hdfs")
    .enableHiveSupport()
    .getOrCreate()
)

logger.info("Spark session initialized")

# ------------------------------------------------------------------------------
# Read Bronze Files
# ------------------------------------------------------------------------------
local_path = "file:///home/jovyan/work/bronze_layer/listings"
logger.info(f"Reading parquet data from {local_path}")

df_listings = (
    spark.read
    .option("mergeSchema", "true")
    .parquet(local_path)
)

row_count = df_listings.count()
logger.info(f"Loaded {row_count} rows")

# ------------------------------------------------------------------------------
# Transform
# ------------------------------------------------------------------------------
logger.info("Adding updated_at_utc_0 column")

df_listings = df_listings.withColumn(
    "updated_at_utc_0",
    F.current_timestamp()
)

# ------------------------------------------------------------------------------
# Write to HDFS
# ------------------------------------------------------------------------------
hdfs_destination = "hdfs://namenode:9000/user/hive/warehouse/airbnb.db/bronze/listings"
logger.info(f"Writing data to HDFS at {hdfs_destination}")

(
    df_listings.write
    .mode("overwrite")
    .partitionBy("extraction_date", "city")
    .format("parquet")
    .save(hdfs_destination)
)

logger.info("HDFS write completed successfully")

# ------------------------------------------------------------------------------
# Hive Metastore Registration
# ------------------------------------------------------------------------------
logger.info("Ensuring Hive database exists")

spark.sql("CREATE DATABASE IF NOT EXISTS airbnb_bronze")

logger.info("Creating external Hive table if not exists")

spark.sql("""
CREATE EXTERNAL TABLE IF NOT EXISTS airbnb_bronze.listings (
    id BIGINT,
    listing_url STRING,
    scrape_id BIGINT,
    last_scraped STRING,
    source STRING,
    name STRING,
    description STRING,
    neighborhood_overview STRING,
    picture_url STRING,
    host_id BIGINT,
    host_url STRING,
    host_name STRING,
    host_since STRING,
    host_location STRING,
    host_about STRING,
    host_response_time STRING,
    host_response_rate STRING,
    host_acceptance_rate STRING,
    host_is_superhost STRING,
    host_thumbnail_url STRING,
    host_picture_url STRING,
    host_neighbourhood STRING,
    host_listings_count DOUBLE,
    host_total_listings_count DOUBLE,
    host_verifications STRING,
    host_has_profile_pic STRING,
    host_identity_verified STRING,
    neighbourhood STRING,
    neighbourhood_cleansed STRING,
    neighbourhood_group_cleansed DOUBLE,
    latitude DOUBLE,
    longitude DOUBLE,
    property_type STRING,
    room_type STRING,
    accommodates BIGINT,
    bathrooms DOUBLE,
    bathrooms_text STRING,
    bedrooms DOUBLE,
    beds DOUBLE,
    amenities STRING,
    price STRING,
    minimum_nights BIGINT,
    maximum_nights BIGINT,
    minimum_minimum_nights DOUBLE,
    maximum_minimum_nights DOUBLE,
    minimum_maximum_nights DOUBLE,
    maximum_maximum_nights DOUBLE,
    minimum_nights_avg_ntm DOUBLE,
    maximum_nights_avg_ntm DOUBLE,
    calendar_updated DOUBLE,
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
    first_review STRING,
    last_review STRING,
    review_scores_rating DOUBLE,
    review_scores_accuracy DOUBLE,
    review_scores_cleanliness DOUBLE,
    review_scores_checkin DOUBLE,
    review_scores_communication DOUBLE,
    review_scores_location DOUBLE,
    review_scores_value DOUBLE,
    license STRING,
    instant_bookable STRING,
    calculated_host_listings_count BIGINT,
    calculated_host_listings_count_entire_homes BIGINT,
    calculated_host_listings_count_private_rooms BIGINT,
    calculated_host_listings_count_shared_rooms BIGINT,
    reviews_per_month DOUBLE,
    updated_at_utc_0 TIMESTAMP           
)
PARTITIONED BY (extraction_date DATE, city STRING)
STORED AS PARQUET
LOCATION '/user/hive/warehouse/airbnb.db/bronze/listings'
""")

logger.info("Repairing Hive partitions")

spark.sql("MSCK REPAIR TABLE airbnb_bronze.listings")

# ------------------------------------------------------------------------------
# Done
# ------------------------------------------------------------------------------
logger.info("Bronze ingestion job completed successfully")

spark.stop()
