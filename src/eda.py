import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/clean_ga4_data.csv")

print("=" * 60)
print("DATASET SHAPE")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("TOP 10 EVENTS")
print("=" * 60)

print(df["event_name"].value_counts().head(10))
print("\n" + "=" * 60)
print("DEVICE DISTRIBUTION")
print("=" * 60)

print(df["device.category"].value_counts())
print("\n" + "=" * 60)
print("BROWSER DISTRIBUTION")
print("=" * 60)

print(df["device.web_info.browser"].value_counts())

print("\n" + "=" * 60)
print("COUNTRY DISTRIBUTION")
print("=" * 60)

print(df["geo.country"].value_counts().head(10))

print("\n" + "=" * 60)
print("TRAFFIC SOURCE")
print("=" * 60)

print(df["traffic_source.source"].value_counts())
print("\n" + "=" * 60)
print("TRAFFIC MEDIUM")
print("=" * 60)

print(df["traffic_source.medium"].value_counts())