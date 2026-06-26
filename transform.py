from pathlib import Path
import json
import pandas as pd

# Read raw JSON
with open("raw/jobs.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data["results"])

print("Rows before cleaning:", len(df))

# Keep useful columns
df = df[
    [
        "id",
        "title",
        "company",
        "location",
        "category",
        "salary_min",
        "salary_max",
        "description"
    ]
].copy()

# Flatten nested columns
df["company"] = df["company"].apply(
    lambda x: x.get("display_name")
    if isinstance(x, dict)
    else None
)

df["location"] = df["location"].apply(
    lambda x: x.get("display_name")
    if isinstance(x, dict)
    else None
)

df["category"] = df["category"].apply(
    lambda x: x.get("label")
    if isinstance(x, dict)
    else None
)

# Remove duplicate jobs
df.drop_duplicates(subset=["id"], inplace=True)

# Remove rows missing important fields
df.dropna(
    subset=["title", "company", "location"],
    inplace=True
)

# Calculate average salary using minimum and maximum salary
df["avg_salary"] = (df["salary_min"] + df["salary_max"]) / 2

# Round to 2 decimal places
df["avg_salary"] = df["avg_salary"].round(2)


# Create clean folder if needed
Path("clean").mkdir(exist_ok=True)

# Save cleaned data
df.to_csv(
    "clean/jobs_clean.csv",
    index=False
)

print("Clean data saved to clean/jobs_clean.csv")