from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime

with DAG(
    dag_id="airbnb_medallion_ELT",
    start_date=datetime(2025, 12, 26),
    schedule_interval=None,   # manual trigger for now
    catchup=False,
    tags=["spark", "airbnb", "pipeline", "elt"],
) as dag:

    run_webscraping = DockerOperator(
        task_id="run_webscraping",
        image="raw-ingest:latest",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",

        mounts=[
            Mount(
                source="C:/Users/teohr/Downloads/UM/Big Data Management/group-asgmt/docker-test/bronze_layer",
                target="/bronze_layer",
                type="bind",
            )
        ],
    )


    # 1️⃣ BRONZE INGESTION
    run_bronze_spark = BashOperator(
        task_id="run_bronze_spark",
        bash_command="""
        docker exec spark-notebook \
          spark-submit \
            --master local[*] \
            --deploy-mode client \
            /home/jovyan/work/bronze/upload_hdfs.py
        """
    )

    # 2️⃣ SILVER TRANSFORMATION (runs AFTER bronze)
    run_silver_spark = BashOperator(
        task_id="run_silver_spark",
        bash_command="""
        docker exec spark-notebook \
          spark-submit \
            --master local[*] \
            --deploy-mode client \
            /home/jovyan/work/silver/stg_listings.py
        """
    )

        # 3️⃣ GOLD TRANSFORMATIONS (runs AFTER silver)
    run_gold_fact_listings = BashOperator(
        task_id="run_gold_fact_listings",
        bash_command="""
        docker exec spark-notebook spark-submit --master local[*] /home/jovyan/work/gold/fct_listings.py
        """
    )

    run_gold_dim_hosts = BashOperator(
        task_id="run_gold_dim_hosts",
        bash_command="""
        docker exec spark-notebook spark-submit --master local[*] /home/jovyan/work/gold/dim_host.py
        """
    )

    run_gold_neighborhood_stats = BashOperator(
        task_id="run_gold_dim_listings",
        bash_command="""
        docker exec spark-notebook spark-submit --master local[*] /home/jovyan/work/gold/dim_listings.py
        """
    )

    # 🧠 DEPENDENCIES
    run_webscraping >> run_bronze_spark
    run_bronze_spark >> run_silver_spark
    run_silver_spark >> [run_gold_fact_listings, run_gold_dim_hosts, run_gold_neighborhood_stats]

