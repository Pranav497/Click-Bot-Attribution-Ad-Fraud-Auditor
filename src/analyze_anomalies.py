import pandas as pd

print("=" * 60)
print("SESSION ANOMALY ANALYSIS")
print("=" * 60)

df = pd.read_csv("data/processed/session_ml_anomalies.csv")

print("\nDataset Shape:")
print(df.shape)
print("\nAnomaly Distribution:")

print(df["ml_anomaly"].value_counts())
anomalies = (df["ml_anomaly"] == 1).sum()

total = len(df)

print("\nAnomaly Percentage:")

print(round(anomalies / total * 100, 2), "%")
print("\nTop Suspicious Sessions")

cols = [
    "session_id",
    "total_engagement_time",
    "avg_engagement_time",
    "event_count",
    "page_view_count",
    "traffic_source",
    "traffic_medium",
    "device_category",
    "browser",
    "country",
    "anomaly_score"
]

print(
    df[df["ml_anomaly"] == 1]
    .sort_values("anomaly_score")
    [cols]
)
print("\nDevice Distribution")

print(
    df[df["ml_anomaly"] == 1]["device_category"]
    .value_counts(dropna=False)
)
print("\nBrowser Distribution")

print(
    df[df["ml_anomaly"] == 1]["browser"]
    .value_counts(dropna=False)
)
print("\nCountry Distribution")

print(
    df[df["ml_anomaly"] == 1]["country"]
    .value_counts(dropna=False)
)
print("\nTraffic Source Distribution")

print(
    df[df["ml_anomaly"] == 1]["traffic_source"]
    .value_counts(dropna=False)
)
suspicious = df[df["ml_anomaly"] == 1]

suspicious.to_csv(
    "data/processed/suspicious_sessions.csv",
    index=False
)

print("\nSuspicious sessions saved successfully!")