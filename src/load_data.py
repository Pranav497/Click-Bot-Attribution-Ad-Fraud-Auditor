import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/ga4_event_2021.csv")

print("=" * 60)
print("First 5 Rows")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("Dataset Shape")
print("=" * 60)
print(df.shape)

print("\n" + "=" * 60)
print("Column Names")
print("=" * 60)
print(df.columns.tolist())

print("\n" + "=" * 60)
print("Dataset Information")
print("=" * 60)
print(df.info())

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(df.isnull().sum())