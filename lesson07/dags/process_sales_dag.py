from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import os
import requests

BASE_DIR = os.environ.get("BASE_DIR")
JOB1_PORT = 8081
JOB2_PORT = 8082


def run_job_1(execution_date=None):
    date_range = ['2022-08-09', '2022-08-10', '2022-08-11'] if execution_date is None else [execution_date]

    for date in date_range:
        raw_dir = os.path.join(BASE_DIR, "raw", "sales", date)

        # Run Job 1
        print(f"Starting job1 for {date}:")
        resp1 = requests.post(
            url=f'http://localhost:{JOB1_PORT}/',
            json={
                "date": date,
                "raw_dir": raw_dir
            }
        )
        assert resp1.status_code == 201
        print("job1 completed!")


def run_job_2(execution_date=None):
    date_range = ['2022-08-09', '2022-08-10', '2022-08-11'] if execution_date is None else [execution_date]

    for date in date_range:
        raw_dir = os.path.join(BASE_DIR, "raw", "sales", date)
        stg_dir = os.path.join(BASE_DIR, "stg", "sales", date)
        # Run Job 2
        print(f"Starting job2 for {date}:")
        resp2 = requests.post(
            url=f'http://localhost:{JOB2_PORT}/',
            json={
                "raw_dir": raw_dir,
                "stg_dir": stg_dir
            }
        )
        assert resp2.status_code == 201
        print("job2 completed!")


# Define default_args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 21),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'process_sales_v5',
    default_args=default_args,
    description='A DAG for processing sales data based on execution date or a specific range',
    schedule_interval='0 1 * * *',  # At 01:00 AM UTC every day
)

# Define the task
task1 = PythonOperator(
    task_id='run_job_1',
    python_callable=run_job_1,
    op_kwargs={'execution_date': '{{ ds }}'},
    provide_context=True,
    dag=dag,
)

task2 = PythonOperator(
    task_id='run_job_2',
    python_callable=run_job_2,
    op_kwargs={'execution_date': '{{ ds }}'},
    provide_context=True,
    dag=dag,
)

task1 >> task2