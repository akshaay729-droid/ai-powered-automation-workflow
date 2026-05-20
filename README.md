**AI-Powered Automation Workflow**

An end-to-end Python automation project that preprocesses customer reviews, performs AI-based sentiment analysis using Hugging Face Transformers, and automatically generates Excel reports and visual charts.

**Project Overview**

This project demonstrates how to automate a complete AI workflow using Python.

**The pipeline:**

Loads raw customer reviews from a CSV file.
Cleans and preprocesses the text.
Runs sentiment analysis using a pre-trained Transformer model.
Generates an Excel report and sentiment chart.
Automates the entire workflow with a single command.

**Features**

Automated text preprocessing
Sentiment analysis using Transformers
Confidence score generation
Excel report export
Bar chart visualization
Modular Python scripts
One-command pipeline execution

**Technologies Used**

Python 3.11+
pandas
matplotlib
transformers
PyTorch
openpyxl
schedule

**Project Structure**

AI AUTOMATION WORKFLOW/
│
├── data/
│   ├── raw_reviews.csv
│   ├── processed_reviews.csv
│   └── final_reviews.csv
│
├── reports/
│   ├── sentiment_report.xlsx
│   └── sentiment_chart.png
│
├── src/
│   ├── preprocess.py
│   ├── sentiment_model.py
│   ├── report_generator.py
│   └── scheduler.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore

**Installation**

1. Get the Project Files

If you already have the project folder on your computer (as you do now), simply open the project in VS Code.

If you upload this project to GitHub later, you can clone it using:

git clone https://github.com/your-username/ai-powered-automation-workflow.git
cd ai-powered-automation-workflow

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt


▶**How to Run**

Run the complete pipeline:

python main.py

Or run the scheduler directly:

python src/scheduler.py

**Sample Output**

Sentiment Summary
POSITIVE    5
NEGATIVE    5
Generated Files
data/processed_reviews.csv
data/final_reviews.csv
reports/sentiment_report.xlsx
reports/sentiment_chart.png

**How the Workflow Works**

1. Preprocessing (preprocess.py)

Loads raw reviews.
Converts text to lowercase.
Removes punctuation and extra spaces.
Saves cleaned reviews.

2. Sentiment Analysis (sentiment_model.py)

Loads a pre-trained sentiment analysis model.
Predicts sentiment and confidence score.
Saves final results.

3. Report Generation (report_generator.py)

Counts positive and negative reviews.
Creates a bar chart.
Exports an Excel report.

4. Workflow Scheduler (scheduler.py)

Executes all modules in sequence.

**Example Results**

Review	Sentiment	Confidence
This product is amazing! I love it.	POSITIVE	0.9999
Terrible quality, very disappointed.	NEGATIVE	0.9998

**Resume Description**

AI-Powered Automation Workflow for Customer Review Sentiment Analysis

Developed an end-to-end Python automation pipeline to preprocess review data, perform sentiment analysis using Hugging Face Transformers, and generate Excel reports with visualizations. Automated repetitive AI tasks through modular scripts and workflow orchestration.

**Future Enhancements**

Streamlit dashboard
Email report automation
Scheduled execution using Windows Task Scheduler
Support for larger datasets
Docker deployment

**Author**

Akshat Agrawal

GitHub: https://github.com/akshaay729-droid
LinkedIn: https://www.linkedin.com/in/akshat-agrawal-11s2004/

**AI-Powered Sentiment Analysis Web App**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

**Live Demo:** https://ai-powered-sentiment-analysis.streamlit.app  
**GitHub:** https://github.com/akshaay729-droid/ai-powered-automation-workflow

## 📸 Application Screenshots

### Home Page
![Home Page](images/screenshot1.png)

### Uploading CSV File
![Upload CSV](images/screenshot2.png)

### Sentiment Analysis Results
![Results](images/screenshot3.png)

### Sentiment Distribution Chart
![Chart](images/screenshot4.png)