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
    subset=[
        "title",
        "company",
        "location",
        "salary_min",
        "salary_max"
    ],
    inplace=True
)

# Calculate average salary using minimum and maximum salary
df["avg_salary"] = (df["salary_min"] + df["salary_max"]) / 2

# Round to 2 decimal places
df["avg_salary"] = df["avg_salary"].round(2)

# Classify salary type
def get_salary_type(row):
    salary = row["avg_salary"]
    desc = str(row["description"]).lower()

    # Annual salaries
    if salary >= 1000:
        return "Annual"

    # Hourly salaries
    hourly_keywords = [
        "per hour",
        "/hour",
        "hourly",
        "hourly rate",
        "p/h",
        "paid per shift",
        "per shift",
        "an hour"
    ]

    if any(keyword in desc for keyword in hourly_keywords):
        return "Hourly"

    # Couldn't determine
    return "Unknown"


df["salary_type"] = df.apply(get_salary_type, axis=1)

# Create clean folder if needed
Path("clean").mkdir(exist_ok=True)


df.to_csv(
    "clean/jobs_clean.csv",
    index=False
)

print("Clean data saved to clean/jobs_clean.csv")