from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import os

def verify_connection():
    hook = PostgresHook(postgres_conn_id='ccda')
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT TO_CHAR(CURRENT_DATE, 'YYYY-MM-DD');")
    
    result = cursor.fetchone()
    if result:
        print(f"Database connection successful. Current date: {result[0]}")
    else:
        raise ValueError("Error: Connection unsuccessful")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 20),
    'retries': 1,
}

dag = DAG(
    'verify_connection',
    default_args=default_args,
    description='Test postgresql connection',
    schedule_interval=None,
    catchup=False,
)

verify_connection = PythonOperator(
    task_id='verify_connection',
    python_callable=verify_connection,
    dag=dag,
)

verify_connection

