import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_model():
    # Define base paths
    base_path = os.path.dirname(__file__)  # dags/
    data_path = os.path.join(base_path, "data", "fake.csv")
    output_dir = os.path.join(base_path, "..", "SavedModels")
    os.makedirs(output_dir, exist_ok=True)

    # Load dataset
    df = pd.read_csv(data_path)
    df = df.dropna()

    # Preprocessing
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    X = tfidf.fit_transform(df['text'].astype(str))
    y = df['label']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    clf = LogisticRegression()
    clf.fit(X_train, y_train)

    # Save model and vectorizer
    with open(os.path.join(output_dir, "model.pkl"), "wb") as f:
        pickle.dump(clf, f)

    with open(os.path.join(output_dir, "fake_news_vectorizer.pkl"), "wb") as f:
        pickle.dump(tfidf, f)

    print("✅ Model training complete and saved to SavedModels/")
