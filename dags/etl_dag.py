from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.etl import etl

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('etl_dag', default_args=default_args, schedule_interval='@daily')

etl_task = PythonOperator(
    task_id='etl_task',
    python_callable=etl,
    dag=dag
)
