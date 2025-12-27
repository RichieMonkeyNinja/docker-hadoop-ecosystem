CREATE USER IF NOT EXISTS spark_admin IDENTIFIED BY 'spark_123';
GRANT ALL ON *.* TO spark_admin WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS airbnb_gold;
GRANT ALL ON airbnb_gold.* TO spark_admin;