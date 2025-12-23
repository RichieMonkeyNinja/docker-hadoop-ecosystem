# Bronze Layer

This .md will cover the following processes in bronze layer.

1) Data Ingestion in local using raw_data_ingestion.ipynb
2) Put the folders inside HDFS and create external table in Hive using spark-notebook.


Note:
1) I have set up the dependencies using uv, run the following commands to create a venv with the necessary libraries and run with the environment.
```powershell
uv sync
```

2) How to activate venv in .ipynb file.

![alt text](bronze_md_ipynb_venv.png)

## Section 1: Data Ingestion

1) Run all the kernels inside raw_data_ingestion.ipynb.
- You will notice some kernels are commented out, the webscrapping parts are commented out as this is currently in development.

2) The output parquet files will be populated inside **bronze_layer/listings/** under the corresponding city and extraction date.

3) Output should look like this:

![alt text](bronze_md_parquet_layout.png)

## Section 2: Upload Data to HDFS

Note: In a medallion architecture following an ELT format, data are ingested and transformed, hence zero transformation except column schema changes are performed.

1. Open the Spark Notebook. 
- Refer to readme.md under **How to Use Spark-Notebook** for guides on how to access Spark Notebook.

2. Run the following .ipynb files:
- /work/bronze/upload_hdfs.ipynb

3. Explaination of upload_hdfs.ipynb below:

![alt text](bronze_md_upload_hdfs_ss1.png)

4. Uploads the data inside HDFS

![alt text](bronze_md_upload_hdfs_ss2.png)

5. Create Database, and Table inside Hive to access via Hive, Beeline, or Trino.

![alt text](bronze_md_upload_hdfs_ss3.png)

![alt text](bronze_md_upload_hdfs_ss4.png)