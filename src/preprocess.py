import pandas as pd
import re


def clean_text(text):
    """
    Clean text by:
    - converting to lowercase
    - removing punctuation and special characters
    - removing extra spaces
    """
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def preprocess_data(
    input_file="data/raw_reviews.csv",
    output_file="data/processed_reviews.csv"
):
    # Load CSV data
    df = pd.read_csv(input_file)

    # Clean the review column
    df["clean_review"] = df["review"].apply(clean_text)

    # Save processed data
    df.to_csv(output_file, index=False)

    print(f"Processed data saved to {output_file}")
    print(df.head())


if __name__ == "__main__":
    preprocess_data()