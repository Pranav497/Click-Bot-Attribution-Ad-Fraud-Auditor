import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/ga4_event_2021.csv")

print("=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
print(df.duplicated().sum())

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)
print(df.dtypes)

print("\n" + "=" * 60)
print("NUMERIC SUMMARY")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("TOP 15 COLUMNS WITH MOST MISSING VALUES")
print("=" * 60)

missing = df.isnull().sum().sort_values(ascending=False)
print(missing.head(15))