# How to Run

1) Install Git and Docker Desktop (if haven't)
2) git clone "https://github.com/RichieMonkeyNinja/docker-hadoop-ecosystem.git"
3) docker compose up -d
4) Have Fun!
5) Please notify me any encountered issues.
6) Please create a new branch for any new features, please don't commit directly on the main branch, submit a merge request and notify Richie Teoh or Elmer Lee to validate the branch and approve the merge request.

# Progress Update (Skeletal Framework)

1) Storage - HDFS (OK)
2) Processing - pySpark notebook (OK)
3) Exploration + Metadata - Hive SQL + Hive Metastore (running on postgreSQL) (OK)
4) OLAP DB - pySpark writes data on Analytics DB (separate postgreSQL) (on-going)

# Future Features (Considerations)
## Feel free to submit your ideas!
### Most of the technologies I selected are based off the popular tech frameworks on Job Sites (LinkedIn, Indeed, etc)

1) Orchestrator - Apache Airflow
2) OLAP DB - ClickHouse
3) (Low Priority) - Cloud, Beeline, Apache Beam (similar to GCP Dataflow)
4) (Low Priority) - Unstructured Data - HBase, MongoDB