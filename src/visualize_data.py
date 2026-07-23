import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Load Cleaned Dataset
# ============================================================

df = pd.read_csv("data/processed/clean_ga4_data.csv")

print("=" * 50)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)
print(df.shape)

# ============================================================
# 1. EVENT DISTRIBUTION
# ============================================================

event_counts = df["event_name"].value_counts()

plt.figure(figsize=(10, 6))

plt.bar(event_counts.index, event_counts.values)

plt.title("Event Distribution")
plt.xlabel("Event Name")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/figures/event_distribution.png")

plt.show()

# ============================================================
# 2. DEVICE DISTRIBUTION
# ============================================================

device_counts = df["device.category"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    device_counts.values,
    labels=device_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Device Distribution")

plt.savefig("reports/figures/device_distribution.png")

plt.show()

# ============================================================
# 3. BROWSER DISTRIBUTION
# ============================================================

browser_counts = df["device.web_info.browser"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(browser_counts.index, browser_counts.values)

plt.title("Browser Distribution")
plt.xlabel("Browser")
plt.ylabel("Number of Users")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("reports/figures/browser_distribution.png")

plt.show()

print("\nAll charts generated successfully!")
# ============================================================
# 4. COUNTRY DISTRIBUTION
# ============================================================

country_counts = df["geo.country"].value_counts()

plt.figure(figsize=(8,5))

plt.bar(country_counts.index, country_counts.values)

plt.title("Country Distribution")
plt.xlabel("Country")
plt.ylabel("Number of Users")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("reports/figures/country_distribution.png")

plt.show()
# ============================================================
# 5. TRAFFIC SOURCE DISTRIBUTION
# ============================================================

source_counts = df["traffic_source.source"].value_counts()

plt.figure(figsize=(10,5))

plt.bar(source_counts.index, source_counts.values)

plt.title("Traffic Source Distribution")
plt.xlabel("Traffic Source")
plt.ylabel("Users")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/figures/traffic_source_distribution.png")

plt.show()
# ============================================================
# 6. TRAFFIC MEDIUM DISTRIBUTION
# ============================================================

medium_counts = df["traffic_source.medium"].value_counts()

plt.figure(figsize=(8,5))

plt.bar(medium_counts.index, medium_counts.values)

plt.title("Traffic Medium Distribution")
plt.xlabel("Traffic Medium")
plt.ylabel("Users")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("reports/figures/traffic_medium_distribution.png")

plt.show()

print("\nAll 6 charts generated successfully!")