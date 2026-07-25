import pandas as pd
from sklearn.ensemble import IsolationForest

# ============================================================
# LOAD SESSION-LEVEL DATA
# ============================================================

df = pd.read_csv(
    "data/processed/session_level_data.csv"
)

print("=" * 60)
print("SESSION-LEVEL ISOLATION FOREST")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

# ============================================================
# SELECT ML FEATURES
# ============================================================

features = [
    "total_engagement_time",
    "avg_engagement_time",
    "event_count",
    "page_view_count",
    "entrance_count"
]

X = df[features].copy()

# ============================================================
# CONVERT TO NUMERIC
# ============================================================

for column in features:
    X[column] = pd.to_numeric(
        X[column],
        errors="coerce"
    )

# Replace missing values
X = X.fillna(0)

print("\nSelected Features:")
print(features)

print("\nMissing Values:")
print(X.isna().sum())

print("\nFeature Statistics:")
print(X.describe())

# ============================================================
# TRAIN ISOLATION FOREST
# ============================================================

print("\n" + "=" * 60)
print("TRAINING ISOLATION FOREST")
print("=" * 60)

model = IsolationForest(
    n_estimators=100,
    contamination=0.10,
    random_state=42
)

model.fit(X)

print("\n✅ Model trained successfully!")

# ============================================================
# PREDICT ANOMALIES
# ============================================================

df["ml_prediction"] = model.predict(X)

# Isolation Forest:
#  1  = Normal
# -1  = Anomaly

df["ml_anomaly"] = 0

df.loc[
    df["ml_prediction"] == -1,
    "ml_anomaly"
] = 1

# ============================================================
# ANOMALY SCORE
# ============================================================

df["anomaly_score"] = model.decision_function(X)

# Lower score = more anomalous

# ============================================================
# ANOMALY DISTRIBUTION
# ============================================================

print("\n" + "=" * 60)
print("SESSION ANOMALY DISTRIBUTION")
print("=" * 60)

print(
    df["ml_anomaly"].value_counts()
)

# ============================================================
# TOP ANOMALOUS SESSIONS
# ============================================================

print("\n" + "=" * 60)
print("TOP ANOMALOUS SESSIONS")
print("=" * 60)

anomalies = df[
    df["ml_anomaly"] == 1
].sort_values(
    "anomaly_score"
)

print(
    anomalies[
        [
            "session_id",
            "total_engagement_time",
            "avg_engagement_time",
            "event_count",
            "page_view_count",
            "entrance_count",
            "anomaly_score"
        ]
    ].head(10)
)

# ============================================================
# SAVE RESULTS
# ============================================================

df.to_csv(
    "data/processed/session_ml_anomalies.csv",
    index=False
)

print(
    "\n✅ Session-level ML results saved successfully!"
)