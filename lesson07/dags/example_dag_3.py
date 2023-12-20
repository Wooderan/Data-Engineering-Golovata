"""
Pyspark submit job example.

To run this DAG you must:
1. Install spark Airflow provider (see bin/install_providers.sh)
2. Create a connection spark_local with Host equal to "local"
(without quotes). Connection type must be "Spark"
3. Set SPARK_SCRIPT_DIR (relative paths don't work in SparkSubmitOperator)
4. Set SALES_CSV and RES_DIR constants
"""
import os
from airflow import DAG

from datetime import datetime

from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


# Attention! Use your local absolute paths here:
SPARK_SCRIPT_DIR = '/home/hunting/projects/r_d/DE-07/lesson_07/dags/'
SALES_CSV = '/home/hunting/projects/r_d/DE-07/lesson_07/dags/data/sales.csv'
RES_DIR = '/home/hunting/projects/r_d/DE-07/lesson_07/dags/data/sales_avg_price/{{ ds }}/'


dag = DAG(
    dag_id="example_dag_3",
    start_date=datetime(2022, 8, 1),
    end_date=datetime(2022, 9, 1),
    schedule_interval='@monthly',
    catchup=True,
)

run_spark_job = SparkSubmitOperator(
    dag=dag,
    task_id='run_spark_job',
    application=os.path.join(SPARK_SCRIPT_DIR, 'pyspark/sales_avg_price.py'),
    conn_id='spark_local',
    total_executor_cores=3,
    application_args=[
        '--sales-csv', SALES_CSV,
        '--res-dir', RES_DIR,
        '--month', '{{ dag_run.logical_date.month }}',
    ]
)

run_spark_job
