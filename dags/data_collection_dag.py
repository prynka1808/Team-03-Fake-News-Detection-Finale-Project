from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'data_collection'))

from collect_data import collect


default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='data_collection_dag',
    default_args=default_args,
    description='Collects real-time data and saves to raw_data',
    schedule_interval='@daily',
    start_date=datetime(2025, 4, 9),
    catchup=False
) as dag:

    collect_task = PythonOperator(
        task_id='collect_data_task',
        python_callable=collect
    )

    collect_task
