import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/ga4_event_2021.csv")

print("=" * 60)
print("ORIGINAL SHAPE")
print("=" * 60)
print(df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df.shape)

# Remove columns where all values are missing
df = df.dropna(axis=1, how="all")

print("\nAfter Removing Empty Columns:")
print(df.shape)

# Save cleaned dataset
df.to_csv("data/processed/clean_ga4_data.csv", index=False)

print("\n✅ Clean dataset saved successfully!")