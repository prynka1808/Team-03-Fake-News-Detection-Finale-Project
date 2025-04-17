from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

def train_model():
    df = pd.read_csv("/opt/airflow/data/collected_data.csv")
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['text'])
    model = PassiveAggressiveClassifier(max_iter=50)
    model.fit(X, df['label'])
    joblib.dump((vectorizer, model), "/opt/airflow/models/model.pkl")

with DAG("model_training_dag", start_date=datetime(2024, 1, 1), schedule_interval="@weekly", catchup=False) as dag:
    task = PythonOperator(task_id="train_model", python_callable=train_model)
