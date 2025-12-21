CREATE USER IF NOT EXISTS spark_admin IDENTIFIED BY 'spark_123';
GRANT ALL ON *.* TO spark_admin WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS analytics_db;
GRANT ALL ON analytics_db.* TO spark_admin;