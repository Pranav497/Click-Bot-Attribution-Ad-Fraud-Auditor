import pandas as pd

# ============================================================
# Load Engineered Dataset
# ============================================================

df = pd.read_csv("data/processed/featured_ga4_data.csv")

print("=" * 60)
print("RULE-BASED BOT DETECTION")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

# ============================================================
# Initialize Risk Score
# ============================================================

df["risk_score"] = 0

# ============================================================
# Rule 1
# Very Low Engagement Time (<10 ms)
# ============================================================

df.loc[
    df["engagement_time"] < 10,
    "risk_score"
] += 1

# ============================================================
# Rule 2
# Page View with Very Low Engagement
# ============================================================

df.loc[
    (df["event_name"] == "page_view") &
    (df["engagement_time"] < 10),
    "risk_score"
] += 1

# ============================================================
# Rule 3
# Direct Traffic with Very Low Engagement
# ============================================================

df.loc[
    (df["traffic_source.source"] == "(direct)") &
    (df["engagement_time"] < 10),
    "risk_score"
] += 1

# ============================================================
# Rule 4
# Desktop User with Very Low Engagement
# ============================================================

df.loc[
    (df["device.category"] == "desktop") &
    (df["engagement_time"] < 10),
    "risk_score"
] += 1

# ============================================================
# Final Bot Flag
# ============================================================

df["bot_flag"] = 0

df.loc[
    df["risk_score"] >= 2,
    "bot_flag"
] = 1

# ============================================================
# Results
# ============================================================

print("\n" + "=" * 60)
print("RISK SCORE DISTRIBUTION")
print("=" * 60)

print(df["risk_score"].value_counts().sort_index())

print("\n" + "=" * 60)
print("BOT FLAG DISTRIBUTION")
print("=" * 60)

print(df["bot_flag"].value_counts())

print("\nBot Percentage:")

print(
    round(
        df["bot_flag"].mean() * 100,
        2
    ),
    "%"
)

# ============================================================
# Show Suspicious Events
# ============================================================

print("\n" + "=" * 60)
print("TOP SUSPICIOUS EVENTS")
print("=" * 60)

print(
    df.loc[
        df["bot_flag"] == 1,
        [
            "event_name",
            "engagement_time",
            "device.category",
            "traffic_source.source",
            "risk_score"
        ]
    ].head(15)
)

# ============================================================
# Save Dataset
# ============================================================

df.to_csv(
    "data/processed/bot_detection_data.csv",
    index=False
)

print("\n✅ Bot detection dataset saved successfully!")