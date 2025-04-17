from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'monitoring'))

from monitor import monitor

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='model_monitoring_dag',
    default_args=default_args,
    description='Monitor model performance daily',
    schedule_interval='@daily',
    start_date=datetime(2025, 4, 9),
    catchup=False
) as dag:

    monitor_task = PythonOperator(
        task_id='monitor_model_task',
        python_callable=monitor
    )

    monitor_task
