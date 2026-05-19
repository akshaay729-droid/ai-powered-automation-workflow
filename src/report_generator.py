import pandas as pd
import matplotlib.pyplot as plt


def generate_report(
    input_file="data/final_reviews.csv",
    output_excel="reports/sentiment_report.xlsx",
    output_chart="reports/sentiment_chart.png"
):
    # Load data
    df = pd.read_csv(input_file)

    # Count sentiments
    sentiment_counts = df["sentiment"].value_counts()

    print("\nSentiment Summary:")
    print(sentiment_counts)

    # Create chart
    plt.figure(figsize=(6, 4))
    sentiment_counts.plot(kind="bar")

    plt.title("Sentiment Analysis Results")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    # Save chart
    plt.savefig(output_chart)

    # Save Excel report
    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Reviews", index=False)
        sentiment_counts.to_frame().to_excel(
            writer,
            sheet_name="Summary"
        )

    print(f"\nExcel report saved to: {output_excel}")
    print(f"Chart saved to: {output_chart}")


if __name__ == "__main__":
    generate_report()