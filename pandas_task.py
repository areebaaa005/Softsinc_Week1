import pandas as pd
import os

# Load dataset
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data", "titanic.csv")

df = pd.read_csv(file_path)

print("✅ Dataset loaded successfully!\n")

# 1️⃣ Task 1: Groupby Analysis (avg survival rate per gender)
print("📊 Average Survival Rate per Gender:")
print(df.groupby("Sex")["Survived"].mean(), "\n")

# 2️⃣ Task 2: Filter data (Females in 1st class who survived)
print("🔍 Females in 1st Class who Survived:")
filtered = df[(df["Sex"] == "female") & (df["Pclass"] == 1) & (df["Survived"] == 1)]
print(filtered[["Name", "Age"]], "\n")

# 3️⃣ Task 3: Clean data (drop NaNs and duplicates)
print("🧹 Dropping missing and duplicate rows...")

before = len(df)
df_cleaned = df.dropna().drop_duplicates()
after = len(df_cleaned)

print(f"Rows before cleaning: {before}")
print(f"Rows after cleaning: {after}")
print(f"🔻 Rows removed: {before - after}")
