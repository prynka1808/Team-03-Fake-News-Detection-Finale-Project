from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/opt/airflow/ml_code')

from model_trainer import train_model  # Only if this function exists

def dummy_test():
    print("Test step executed")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('fake_news_detection_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    train = PythonOperator(
        task_id='train_model_task',
        python_callable=train_model
    )

    test = PythonOperator(
        task_id='test_step',
        python_callable=dummy_test
    )

    train >> test
