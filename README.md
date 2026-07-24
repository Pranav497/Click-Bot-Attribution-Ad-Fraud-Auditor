# 🛡️ Click-Bot Attribution & Ad-Fraud Auditor

A Data Analytics and Machine Learning project that detects suspicious bot traffic in Google Analytics 4 (GA4) event data using Python, feature engineering, rule-based detection, and anomaly detection techniques.

---

## 📌 Project Overview

Digital marketing campaigns often receive invalid traffic from bots, automated scripts, and fake clicks. This project analyzes Google Analytics 4 (GA4) event data to identify suspicious user behavior, improve traffic quality, and support more accurate marketing decisions.

The project follows a complete data analytics workflow:

- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Rule-Based Bot Detection
- Machine Learning (Upcoming)
- Power BI Dashboard (Upcoming)

---

## 🎯 Objectives

- Clean and preprocess GA4 event data.
- Perform exploratory data analysis.
- Visualize user behavior.
- Engineer meaningful features.
- Detect suspicious traffic using rule-based logic.
- Build an Isolation Forest anomaly detection model.
- Create an interactive Power BI dashboard.
- Generate actionable marketing insights.

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Power BI
- Git & GitHub

---

## 📂 Project Structure

```
Click-Bot-Attribution-Ad-Fraud-Auditor/
│
├── data/
│   ├── raw/
│   │   └── ga4_event_2021.csv
│   │
│   └── processed/
│       ├── clean_ga4_data.csv
│       ├── featured_ga4_data.csv
│       └── bot_detection_data.csv
│
├── src/
│   ├── load_data.py
│   ├── data_quality.py
│   ├── clean_data.py
│   ├── explore_data.py
│   ├── visualize_data.py
│   ├── feature_engineering.py
│   └── bot_detection.py
│
├── outputs/
│   └── charts/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ✅ Progress

| Stage | Status |
|--------|--------|
| Project Setup | ✅ |
| Data Loading | ✅ |
| Data Understanding | ✅ |
| Data Cleaning | ✅ |
| Exploratory Data Analysis | ✅ |
| Data Visualization | ✅ |
| Feature Engineering | ✅ |
| Rule-Based Bot Detection | ✅ |
| Isolation Forest | ⏳ |
| Power BI Dashboard | ⏳ |
| Marketing Insights | ⏳ |

---

# 📊 Exploratory Data Analysis

The cleaned dataset contains:

- **210 rows**
- **55 columns**

### Event Distribution

- Page Views
- Scroll Events
- Session Starts
- User Engagement
- Promotions
- Item Views

### Device Distribution

- Desktop
- Mobile

### Browser Distribution

- Chrome
- Safari
- Edge

### Geographic Analysis

- United States
- Qatar

### Traffic Sources

- Google
- Direct
- Referral
- Organic

---

# ⚙️ Feature Engineering

Created the following features:

| Feature | Description |
|----------|-------------|
| engagement_time | User engagement time (milliseconds) |
| session_number | Session count |
| engaged_session | Engaged session indicator |
| entrance_flag | Landing page indicator |

---

# 🤖 Rule-Based Bot Detection

Implemented a rule-based fraud detection system using multiple behavioral indicators.

### Rules

- Very low engagement time
- Page views with very low engagement
- Direct traffic with very low engagement
- Desktop traffic with very low engagement

Each triggered rule contributes to a **Risk Score**.

```
Risk Score >= 2
↓

Bot
```

---

## 📈 Current Results

| Metric | Value |
|---------|------:|
| Total Events | 210 |
| Suspected Bots | 1 |
| Normal Events | 209 |
| Bot Percentage | 0.48% |

---

# 📷 Visualizations

Generated charts include:

- Event Distribution
- Device Distribution

More dashboards will be added using Power BI.

---

# 🚀 Upcoming Work

- Isolation Forest anomaly detection
- Compare ML vs Rule-Based detection
- Power BI dashboard
- Marketing insights
- Adjusted ROAS analysis

---

# 💻 How to Run

Clone the repository

```bash
git clone https://github.com/Pranav497/Click-Bot-Attribution-Ad-Fraud-Auditor.git
```

Move into the project

```bash
cd Click-Bot-Attribution-Ad-Fraud-Auditor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run scripts

```bash
python src/load_data.py

python src/clean_data.py

python src/explore_data.py

python src/visualize_data.py

python src/feature_engineering.py

python src/bot_detection.py
```

---

# 📅 Roadmap

- [x] Data Loading
- [x] Data Cleaning
- [x] EDA
- [x] Visualization
- [x] Feature Engineering
- [x] Rule-Based Bot Detection
- [ ] Isolation Forest
- [ ] Power BI Dashboard
- [ ] Marketing Insights

---

# 📜 License

This project is created for educational purposes and portfolio demonstration.

---

## 👨‍💻 Author

**Pranav Pawar**

GitHub: https://github.com/Pranav497