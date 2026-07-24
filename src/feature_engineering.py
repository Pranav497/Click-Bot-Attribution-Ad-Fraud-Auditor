import pandas as pd

# ============================================================
# Load Clean Dataset
# ============================================================

df = pd.read_csv("data/processed/clean_ga4_data.csv")

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# ============================================================
# Create New Features
# ============================================================

df["engagement_time"] = None
df["session_number"] = None
df["engaged_session"] = None
df["entrance_flag"] = None

# Engagement Time
mask = df["event_params.key"] == "engagement_time_msec"
df.loc[mask, "engagement_time"] = df.loc[mask, "event_params.value.int_value"]

# Session Number
mask = df["event_params.key"] == "ga_session_number"
df.loc[mask, "session_number"] = df.loc[mask, "event_params.value.int_value"]

# Engaged Session
mask = df["event_params.key"] == "engaged_session_event"
df.loc[mask, "engaged_session"] = df.loc[mask, "event_params.value.int_value"]

# Entrance Flag
mask = df["event_params.key"] == "entrances"
df.loc[mask, "entrance_flag"] = df.loc[mask, "event_params.value.int_value"]

# ============================================================
# Convert Features to Numeric
# ============================================================

features = [
    "engagement_time",
    "session_number",
    "engaged_session",
    "entrance_flag"
]

for feature in features:
    df[feature] = pd.to_numeric(df[feature], errors="coerce")

# ============================================================
# Display Summary
# ============================================================

print("\nFeature Summary\n")

print(df[features].describe())

# ============================================================
# Save Engineered Dataset
# ============================================================

df.to_csv(
    "data/processed/featured_ga4_data.csv",
    index=False
)

print("\n✅ Engineered dataset saved successfully!")