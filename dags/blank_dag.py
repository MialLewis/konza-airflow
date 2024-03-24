from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_world():
    print("Hello World")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 20),
    'retries': 1,
}

dag = DAG(
    'blank_dag',
    default_args=default_args,
    description='blank dag, prints Hello World',
    schedule_interval=None,
    catchup=False,
)

blank_task = PythonOperator(
    task_id='blank_task',
    python_callable=hello_world,
    dag=dag,
)

blank_task

