from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("✅ Hello from Airflow!")
    return "Success"

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='sample_logging_dag',
    default_args=default_args,
    description='A simple test DAG that prints a message',
    schedule_interval='@daily',
    start_date=datetime(2025, 4, 7),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello
    )

    task1
