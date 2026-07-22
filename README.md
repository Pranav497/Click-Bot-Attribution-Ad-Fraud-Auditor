# 🤖 Click-Bot Attribution & Ad-Fraud Auditor

A Data Analytics & Machine Learning project that detects suspicious bot traffic in Google Analytics data, cleans marketing attribution, and calculates more accurate Return on Ad Spend (ROAS).

---

## 📌 Problem Statement

Digital marketing campaigns often suffer from bot traffic and fraudulent interactions that inflate website visits, clicks, and conversions. This leads to incorrect marketing decisions and wasted advertising budgets.

This project builds a Python-based auditing system that analyzes Google Analytics data, identifies suspicious traffic patterns, and provides cleaner marketing insights.

---

# 🎯 Objectives

- Clean Google Analytics data
- Analyze user behavior
- Detect suspicious traffic patterns
- Build an anomaly detection model using Isolation Forest
- Create Power BI dashboards
- Calculate adjusted ROAS after removing suspected bot traffic

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib *(Coming Soon)*
- Scikit-Learn *(Coming Soon)*
- Power BI *(Coming Soon)*
- Git & GitHub
- VS Code

---

# 📂 Project Structure

```
Click-Bot-Attribution-Ad-Fraud-Auditor
│
├── data
│   ├── raw
│   └── processed
│
├── src
│   ├── main.py
│   ├── load_data.py
│   ├── explore_data.py
│   ├── data_quality.py
│   ├── clean_data.py
│   └── eda.py
│
├── reports
│   └── figures (Coming Soon)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dataset

Dataset Used:

**Google Analytics 4 Obfuscated Sample Ecommerce Dataset**

Source:

https://www.kaggle.com/datasets/google/google-analytics-sample

---

# ✅ Progress

## Day 1
- Project setup
- Virtual environment configuration
- GitHub repository created
- Loaded GA4 dataset
- Verified project structure

---

## Day 2
- Explored dataset structure
- Understood important GA4 columns
- Learned event-level analytics
- Identified business-relevant features

---

## Day 3
### Data Cleaning

- Removed duplicate records
- Removed completely empty columns
- Created processed dataset
- Performed data quality assessment

### Results

Original Dataset

```
500 Rows × 94 Columns
```

After Cleaning

```
210 Rows × 55 Columns
```

---

## Day 4
### Exploratory Data Analysis (EDA)

Analyzed:

- Event Distribution
- Device Distribution
- Browser Distribution
- Country Distribution
- Traffic Source
- Traffic Medium

### Key Insights

### Event Distribution

| Event | Count |
|--------|------:|
| page_view | 13 |
| scroll | 11 |
| session_start | 8 |
| view_promotion | 7 |
| user_engagement | 7 |

---

### Device Distribution

| Device | Count |
|--------|------:|
| Desktop | 37 |
| Mobile | 18 |

---

### Browser Distribution

| Browser | Count |
|---------|------:|
| Chrome | 43 |
| Safari | 9 |
| Edge | 2 |

---

### Country Distribution

| Country | Count |
|---------|------:|
| United States | 37 |
| Qatar | 18 |

---

### Traffic Sources

| Source | Count |
|---------|------:|
| Google | 20 |
| Direct | 13 |
| Referral | 15 |

---

# 📈 Current Workflow

```
Google Analytics Dataset
        │
        ▼
Load Data ✅
        │
        ▼
Explore Dataset ✅
        │
        ▼
Data Quality Check ✅
        │
        ▼
Data Cleaning ✅
        │
        ▼
Exploratory Data Analysis ✅
        │
        ▼
Data Visualization 🔄
        │
        ▼
Feature Engineering
        │
        ▼
Bot Detection
        │
        ▼
Isolation Forest
        │
        ▼
Power BI Dashboard
        │
        ▼
Adjusted ROAS
```

---

# 🚀 Upcoming Features

- Data Visualization using Matplotlib
- Feature Engineering
- Rule-Based Bot Detection
- Isolation Forest Model
- Bot Traffic Scoring
- Power BI Dashboard
- Marketing Attribution Audit
- Adjusted ROAS Calculation

---

# 💡 Business Value

This project demonstrates how Data Analytics and Machine Learning can improve digital marketing decisions by:

- Removing misleading traffic
- Improving campaign analysis
- Detecting suspicious behavior
- Producing more reliable marketing KPIs
- Helping businesses allocate advertising budgets more effectively

---

# 🎯 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Python Programming
- Pandas
- Git & GitHub
- Marketing Analytics
- Business Intelligence
- Data Quality Assessment

---

# 📅 Current Status

**Project Progress:** **40% Complete**

```
████████████████░░░░░░░░░░

✅ Project Setup
✅ Data Loading
✅ Data Understanding
✅ Data Cleaning
✅ Exploratory Data Analysis

🔄 Data Visualization

⬜ Feature Engineering
⬜ Bot Detection
⬜ Isolation Forest
⬜ Power BI Dashboard
⬜ Final Report
```

---

# 👨‍💻 Author

**Pranav Pawar**

B.Tech Computer Science Engineering

GitHub: https://github.com/Pranav497