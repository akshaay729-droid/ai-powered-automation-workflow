import os


def run_pipeline():
    print("Step 1: Preprocessing data...")
    os.system("python src/preprocess.py")

    print("\nStep 2: Running sentiment analysis...")
    os.system("python src/sentiment_model.py")

    print("\nStep 3: Generating reports...")
    os.system("python src/report_generator.py")

    print("\nAI Automation Workflow Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()