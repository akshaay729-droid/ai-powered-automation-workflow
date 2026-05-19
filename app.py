import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import re

st.set_page_config(
    page_title="AI Sentiment Analysis",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Sentiment Analysis")
st.write("Upload a CSV file with a 'review' column.")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "POSITIVE"
    elif polarity < 0:
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"

    confidence = abs(polarity)
    return sentiment, confidence

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Data")
    st.dataframe(df.head())

    if "review" not in df.columns:
        st.error("CSV must contain a column named 'review'.")
        st.stop()

    if st.button("🚀 Run Sentiment Analysis"):
        df["clean_review"] = df["review"].apply(clean_text)

        sentiments = df["clean_review"].apply(analyze_sentiment)

        df["sentiment"] = sentiments.apply(lambda x: x[0])
        df["confidence"] = sentiments.apply(lambda x: x[1])

        st.success("Analysis completed!")

        st.subheader("📊 Results")
        st.dataframe(df)

        summary = df["sentiment"].value_counts()

        st.subheader("📈 Sentiment Summary")
        st.write(summary)

        fig, ax = plt.subplots()
        summary.plot(kind="bar", ax=ax)
        ax.set_ylabel("Count")
        ax.set_title("Sentiment Distribution")
        st.pyplot(fig)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Download Results CSV",
            csv,
            "sentiment_results.csv",
            "text/csv"
        )