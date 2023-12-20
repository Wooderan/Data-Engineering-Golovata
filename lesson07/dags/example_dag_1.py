from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


DEFAULT_ARGS = {
    'depends_on_past': False,
    'email': ['admin@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': 30,
}


dag = DAG(
    dag_id='example_dag_1',
    start_date=datetime(2023, 1, 9),
    # end_date=datetime(2023, 1, 15),
    schedule_interval="0 5 * * *",
    # schedule_interval="@daily" # <-- after midnight,
    catchup=True,
    default_args=DEFAULT_ARGS,
)

task1 = EmptyOperator(
    task_id='task1',
    dag=dag,
)

task2 = BashOperator(
    task_id='task2',
    dag=dag,
    bash_command="echo Hello world",
)

task3 = BashOperator(
    task_id='task3',
    dag=dag,
    bash_command="echo Hello world again",
)

task4 = EmptyOperator(
    task_id='task4',
    dag=dag,
)

task5 = EmptyOperator(
    task_id='task5',
    dag=dag,
    email='friend@example.com'
)


task1 >> [task2, task3] >> task4 >> task5

# another way:
# task1.set_downstream(task2)
# task2.set_upstream(task1)


