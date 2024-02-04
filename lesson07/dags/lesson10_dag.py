from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
import requests
import json

AUTH_TOKEN = '2b8d97ce57d401abd89f45b0079d8790edd940e6'

def get_sales(**kwargs):
    date = kwargs['ds']
    results = []

    page = 0
    while True:
        page += 1
        response = requests.get(
            url='https://fake-api-vycpfa6oca-uc.a.run.app/sales',
            params={'date': date, 'page': page},
            headers={'Authorization': AUTH_TOKEN},
        )
        if response.status_code == 200:
            page_data = response.json()
            if page_data:
                results.extend(page_data)
            else:
                break
        else:
            break

    filename = f'/tmp/sales_data_{date}.json'
    with open(filename, 'w') as f:
        json.dump(results, f)

    return filename

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sales_data_pipeline_lesson10_v2',
    default_args=default_args,
    description='A simple pipeline to fetch sales data and upload to GCS',
    schedule_interval=timedelta(days=1),
)

download_sales_data = PythonOperator(
    task_id='get_sales_data',
    python_callable=get_sales,
    provide_context=True,
    dag=dag,
)

# Задача для загрузки данных в GCS
upload_to_gcs = LocalFilesystemToGCSOperator(
    task_id='upload_sales_data_to_gcs',
    src="{{ task_instance.xcom_pull(task_ids='get_sales_data') }}",
    dst='src1/sales/v1/{{ ds_nodash[:4] }}/{{ ds_nodash[4:6] }}/{{ ds_nodash[6:8] }}/sales_data.json',
    bucket='de-07-test-bucket',
    dag=dag,
)

download_sales_data >> upload_to_gcs
