# How to Run

1) Install Git and Docker Desktop (if haven't)
2) git clone "https://github.com/RichieMonkeyNinja/docker-hadoop-ecosystem.git"
3) docker compose up -d
4) Have Fun! Refer to Individual "How to Use" tutorial to access different tools.
5) Please please notify me any encountered issues.
6) Please create a new branch for any new features, please don't commit directly on the main branch, submit a merge request and notify Richie Teoh or Elmer Lee to validate the branch and approve the merge request.

# How to Use Spark-Notebook

1) 
```powershell
 docker logs spark-notebook
 ```

2) You should see something like this, randomly generated 48 tokens behind the localhost URL for access purposes. Copy-paste the URL into your favorite browser to start exploring Spark!

(Note: Copy the http://127.0.0.1:8888/lab? version, as it is the most consistent for my windows OS)
![alt text](readme_images/image.png)

3) You should see this webpage once loaded.
![alt text](readme_images/image-1.png)

- The mounted folder is inside ./work/, please save your work that is ready to push inside  the ./work/ folder.

- Else, it will be destroyed once docker-compose down.

4) Refer to ./work/spark_template.ipynb to get a rough idea of Spark functionality. 

5) PySpark Resources//Documentation: https://spark.apache.org/docs/latest/api/python/user_guide/index.html



# How to Create a New Branch - Git & GitHub
1. git checkout -b "branch_name" (remember the quotations mark "")
2. git add <file_1> <file_2> ... <file_n> or git add . (git add <file_n> is a better practice in the real world.)
3. git commit -m "message" - make sure your message conveys the idea clearly and commit frequently to be safe.
4. git push origin <branch_name> - push your branch into GitHub repository
5. Go to GitHub -> Submit merge request -> Notify Richie Teoh//Elmer Lee to review
6. Hooray! Your code is reviewed and approved and merged into the main branch, thanks for your work!

# How to Write data into Apache Clickhouse via Spark Notebook

1. 
```python
spark = SparkSession.builder.getOrCreate()

ch_url = "jdbc:ch://analytics-clickhouse:8123/default?user=spark_admin&password=spark_123"

ch_properties = {
    "driver": "com.clickhouse.jdbc.ClickHouseDriver",
    "createTableOptions": "ENGINE = MergeTree() ORDER BY (col_pk, col_pk2)"

df.write.jdbc(
        url=ch_url, 
        table="random_sensor_data", 
        mode="overwrite", 
        properties=ch_properties
    )    
}
```

# How to access Clickhouse

## Testing & Playing
1) Login http://localhost:8123/play?user=spark_admin&password=spark_123

2) Play with your favourite SQL queries!

## Connect to dbeaver (Better IntelliSense)

1) If Windows OS, can directly download dbeaver from Microsoft Store. Else, can install dbeaver Community Edition directly from webpages. Else, god bless you.

2) ![alt text](readme_images/image-2.png)

3) ![alt text](readme_images/image-3.png)

# How to use Power BI to connect with Clickhouse

1) Install Power BI from Microsoft Store (Windows OS), else God Bless you.
2) Install ClickHouse ODBC Driver from this site: https://github.com/ClickHouse/clickhouse-odbc/releases
3) Personally, I (Richie) installed 1.5.0.20251127 as the later versions are BETA as of 21/12/2025.

![alt text](readme_images/image-4.png)

4) Now, you can connect to ClickHouse via Power BI similar to any other databases! 

Continue reading below if first-time or new to Power BI:

5) In the top navigation bar, click **Transform Data** to enter **Power Query Editor** (backend of Power BI to extract data).

![alt text](readme_images/image-5.png)

6) Select **New Source** -> **More** -> **ClickHouse**
![alt text](readme_images/image-6.png)

7) Host: localhost, Port: 8123, Database: default, Username: spark_admin, Password: spark_123
![alt text](readme_images/image-7.png)

8) Yipee, you connected successfully (hopefully) with ClickHouse ODBC Driver!

9) As of 21/12/2025, this is the snapshot of the UM x Airbnb Power BI template design, feel free to pitch your ideas.

![alt text](readme_images/image-9.png)

# Progress Update (Skeletal Framework)

1) Storage - HDFS (OK)
2) Processing - pySpark notebook (OK)
3) Exploration + Metadata - Hive SQL + Hive Metastore (running on postgreSQL) (OK)
4) OLAP DB - pySpark writes data on Analytics OLAP DB (Apache ClickHouse) (OK)
5) Power BI Template - (OK)

# Future Features (Considerations)
## Feel free to submit your ideas!
### Most of the technologies I selected are based off the popular tech frameworks on Job Sites (LinkedIn, Indeed, etc)

1) Orchestrator - Apache Airflow
2) ~~OLAP DB - ClickHouse~~
3) (Low Priority) - Cloud, Beeline, Apache Beam (similar to GCP Dataflow)
4) (Low Priority) - Unstructured Data - HBase, MongoDB