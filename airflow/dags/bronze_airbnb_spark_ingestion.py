from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bronze_airbnb_spark_ingestion",
    start_date=datetime(2025, 12, 26),
    schedule_interval=None,   # manual trigger for now
    catchup=False,
    tags=["spark", "bronze", "airbnb"],
) as dag:

    run_spark_job = BashOperator(
        task_id="run_bronze_spark",
        bash_command="""
        docker exec spark-notebook \
        spark-submit \
          --master local[*] \
          --deploy-mode client \
          /home/jovyan/work/bronze/upload_hdfs.py
        """
    )
