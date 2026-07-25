# 🛡️ Click-Bot Attribution & Ad-Fraud Auditor

A Data Analytics and Machine Learning project that analyzes Google Analytics 4 (GA4) event data to identify suspicious traffic, detect potential bot behavior, and improve the reliability of digital marketing attribution.

The project combines data cleaning, exploratory data analysis, feature engineering, rule-based detection, session-level analysis, and Isolation Forest anomaly detection.

---

## 📌 Project Overview

Digital marketing campaigns can receive invalid traffic from bots, automated scripts, and unusual user behavior. This can distort engagement metrics and make marketing performance appear better or worse than it actually is.

This project processes GA4 event data to:

- Clean and validate analytics data
- Understand user and traffic behavior
- Engineer behavioral features
- Detect suspicious activity using rule-based logic
- Aggregate event data into sessions
- Detect anomalous sessions using Isolation Forest
- Compare rule-based and machine-learning results
- Prepare data for a Power BI marketing dashboard

---

## 🎯 Objectives

- Clean and preprocess GA4 event data
- Understand the structure of flattened GA4 exports
- Perform exploratory data analysis
- Visualize traffic and user behavior
- Create behavioral features
- Detect suspicious traffic using rule-based detection
- Create session-level features
- Apply Isolation Forest anomaly detection
- Compare rule-based and ML results
- Build a Power BI dashboard
- Generate marketing and attribution insights
- Analyze adjusted marketing performance after suspicious traffic filtering

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Power BI
- Git
- GitHub

---

# 📂 Project Structure

```text
Click-Bot-Attribution-Ad-Fraud-Auditor/
│
├── data/
│   ├── raw/
│   │   └── ga4_event_2021.csv
│   │
│   └── processed/
│       ├── clean_ga4_data.csv
│       ├── featured_ga4_data.csv
│       ├── bot_detection_data.csv
│       ├── ml_bot_detection_data.csv
│       └── session_level_data.csv
│
├── src/
│   ├── load_data.py
│   ├── data_quality.py
│   ├── clean_data.py
│   ├── explore_data.py
│   ├── visualize_data.py
│   ├── feature_engineering.py
│   ├── bot_detection.py
│   ├── isolation_forest.py
│   └── session_features.py
│
├── outputs/
│   └── charts/
│
├── README.md
├── requirements.txt
└── .gitignore