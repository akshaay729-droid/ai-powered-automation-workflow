from transformers import pipeline
import pandas as pd


def run_sentiment_analysis(
    input_file="data/processed_reviews.csv",
    output_file="data/final_reviews.csv"
):
    # Load sentiment analysis model
    print("Loading sentiment analysis model...")
    classifier = pipeline("sentiment-analysis")

    # Read processed data
    print("Reading processed reviews...")
    df = pd.read_csv(input_file)

    # Run sentiment analysis
    print("Analyzing sentiments...")
    results = classifier(df["clean_review"].tolist())

    # Add results to DataFrame
    df["sentiment"] = [result["label"] for result in results]
    df["confidence"] = [result["score"] for result in results]

    # Save final output
    df.to_csv(output_file, index=False)

    print(f"Sentiment analysis completed!")
    print(f"Results saved to {output_file}")
    print(df[["review", "sentiment", "confidence"]].head())


if __name__ == "__main__":
    run_sentiment_analysis()