from datetime import datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.models.param import Param

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 20),
    'retries': 1,
}

dag = DAG(
    'create_cdd_table',
    default_args=default_args,
    description='creates table from mounted ccd data',
    schedule_interval=None,
    catchup=False,
    params={"XML_FILE_NAME": ""},
)

create_tbl_task = PostgresOperator(
    task_id='create_table_task',
    sql="""
    CREATE TABLE IF NOT EXISTS ccd_ingest_test (
        file_name VARCHAR(225) NOT NULL,
        xml_contents XML NOT NULL
    );
    """,
    postgres_conn_id='ccda',
    dag=dag,
)


ingest_data_task = PostgresOperator(
    task_id='ingest_data_task',
    sql=(
    "INSERT INTO ccd_ingest_test (file_name, xml_contents)"
    "VALUES ('/var/lib/postgresql/xml_files/{{params.XML_FILE_NAME}}', xmlparse(content convert_from(pg_read_binary_file('/var/lib/postgresql/xml_files/{{params.XML_FILE_NAME}}'), 'UTF8')));"
    ),
    postgres_conn_id='ccda',
    dag=dag,
)

create_tbl_task >> ingest_data_task

