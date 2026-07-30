# 🛡️ Click-Bot Attribution & Ad-Fraud Auditor

> Detect suspicious website sessions using Machine Learning and visualize fraudulent traffic using an interactive Power BI dashboard.

![Dashboard]([./images/full-dashboard.png](https://github.com/Pranav497/Click-Bot-Attribution-Ad-Fraud-Auditor/blob/main/dashboard/Full%20Dashboard.png))

---

# 📌 Project Overview

Digital advertising loses billions of dollars every year due to invalid clicks and bot traffic.

This project analyzes Google Analytics session data, detects suspicious user sessions using Machine Learning, and builds an interactive Power BI dashboard to help marketers identify fraudulent traffic.

The dashboard allows users to monitor:

- Total website sessions
- Suspicious (bot) sessions
- Normal sessions
- Bot traffic percentage
- Average engagement time
- Device-wise traffic
- Browser distribution
- Country distribution
- Traffic source analysis

---

# 🚀 Features

✔ Data Cleaning using Python

✔ Exploratory Data Analysis (EDA)

✔ Feature Engineering

✔ Isolation Forest Machine Learning model

✔ Bot Traffic Detection

✔ Interactive Power BI Dashboard

✔ Business KPI Cards

✔ Dynamic Charts

✔ Professional Dashboard Design

---

# 🛠 Tech Stack

| Tool | Purpose |
|-------|---------|
| Python | Data Processing |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Scikit-Learn | Machine Learning |
| Matplotlib | Visualization |
| Power BI | Dashboard |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 📂 Dataset

Source:

Google Analytics 4 Ecommerce Dataset

The dataset contains website session information including:

- Session ID
- Device Category
- Browser
- Country
- Traffic Source
- Engagement Time
- Page Views
- Events
- Entrance Count

---

# ⚙ Project Workflow

```text
Google Analytics Dataset
            │
            ▼
     Data Cleaning
            │
            ▼
 Exploratory Data Analysis
            │
            ▼
 Feature Engineering
            │
            ▼
 Isolation Forest Model
            │
            ▼
 ML Prediction
            │
            ▼
 Power BI Dashboard
```

---

# 📊 Dashboard Preview

## Full Dashboard

![Dashboard](./images/full-dashboard.png)

---

## Device Analysis

Shows session distribution across Desktop, Mobile and Tablet users.

![Device](./images/session-desktop.png)

---

## Country Analysis

Visualizes website traffic by country.

![Country](./images/session-country.png)

---

# 📈 Dashboard KPIs

The dashboard displays

- Total Sessions
- Suspicious Sessions
- Normal Sessions
- Bot Percentage
- Average Engagement Time

Additional visualizations include

- Sessions by Device
- Sessions by Browser
- Sessions by Country
- Sessions by Traffic Source
- Normal vs Suspicious Sessions

---

# 🤖 Machine Learning

Model Used

Isolation Forest

Purpose

Detect anomalous website sessions that may indicate:

- Click Fraud
- Automated Bots
- Invalid Traffic

Prediction Labels

| Value | Meaning |
|------|----------|
| -1 | Suspicious Session |
| 1 | Normal Session |

---

# 📁 Project Structure

```text
Click-Bot-Attribution-Ad-Fraud-Auditor
│
├── data
│   ├── raw
│   ├── processed
│
├── images
│   ├── full-dashboard.png
│   ├── session-desktop.png
│   ├── session-country.png
│
├── src
│   ├── load_data.py
│   ├── clean_data.py
│   ├── explore_data.py
│   ├── feature_engineering.py
│   ├── visualize_data.py
│   └── model.py
│
├── Click-Bot.pbix
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📊 Insights

Some observations from the analysis:

- Desktop users generated the highest number of sessions.
- Chrome contributed the largest share of traffic.
- Most traffic originated from Google search.
- Only a small percentage of sessions were classified as suspicious.
- Low-engagement sessions were more likely to be identified as bot traffic.

---

# 📸 Screenshots

### Dashboard Overview

![Dashboard](./images/full-dashboard.png)

---

### Device Distribution

![Desktop](./images/session-desktop.png)

---

### Country Distribution

![Country](./images/session-country.png)

---

# ▶ How to Run

Clone the repository

```bash
git clone https://github.com/Pranav497/Click-Bot-Attribution-Ad-Fraud-Auditor.git
```

Go inside project

```bash
cd Click-Bot-Attribution-Ad-Fraud-Auditor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python src/main.py
```

Open

```
Click-Bot.pbix
```

using Power BI Desktop.

---

# 📌 Future Improvements

- Real-time GA4 API integration
- Streamlit Web App
- Fraud Alert Notifications
- Advanced ML Models
- SHAP Explainability
- Time Series Bot Detection

---

# 👨‍💻 Author

**Pranav Pawar**

B.Tech Computer Science

Data Analytics | Machine Learning | Power BI

GitHub

https://github.com/Pranav497

LinkedIn

(Add your LinkedIn URL)

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork it

📢 Share it
