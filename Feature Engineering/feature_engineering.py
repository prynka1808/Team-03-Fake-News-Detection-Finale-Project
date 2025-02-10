import pandas as pd
import nltk
from textblob import TextBlob
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

def add_features(df):
    # Number of words in the text
    df['word_count'] = df['text'].apply(lambda x: len(x.split()))
    
    # Number of characters in the text
    df['char_count'] = df['text'].apply(lambda x: len(x))
    
    # Average word length
    df['avg_word_length'] = df['char_count'] / (df['word_count'] + 1)
    
    # Sentiment polarity using TextBlob
    df['sentiment_polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Sentiment subjectivity using TextBlob
    df['sentiment_subjectivity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    
    # Count of stopwords
    stop_words = set(stopwords.words('english'))
    df['stopword_count'] = df['text'].apply(lambda x: len([word for word in x.split() if word.lower() in stop_words]))
    
    # Ratio of stopwords to total words
    df['stopword_ratio'] = df['stopword_count'] / (df['word_count'] + 1)
    
    # Presence of numbers (binary feature)
    df['contains_numbers'] = df['text'].apply(lambda x: any(char.isdigit() for char in x)).astype(int)
    
    # Uppercase word count
    df['uppercase_word_count'] = df['text'].apply(lambda x: len([word for word in x.split() if word.isupper()]))
    
    return df

if __name__ == "__main__":
    # Load dataset (Replace with your actual dataset path)
    file_path = "Dataset/processed_with_features.csv"
    df = pd.read_csv(file_path)

    # Add new features
    df = add_features(df)

    # Save the updated dataset
    df.to_csv("Dataset/processed_with_more_features.csv", index=False)
    print("Feature engineering completed and saved!")
