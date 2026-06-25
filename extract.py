from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")

all_jobs = []

for page in range(1, 11):  # pages 1-5

    url = f"https://api.adzuna.com/v1/api/jobs/gb/search/{page}"

    params = {
        "app_id": app_id,
        "app_key": app_key,
        "results_per_page": 50
    }
    
    response = requests.get(url, params=params, timeout=30)

    data = response.json()

    all_jobs.extend(data["results"])

    print(f"Downloaded page {page}")

print(f"Total jobs collected: {len(all_jobs)}")

with open("raw/jobs.json", "w") as f:
    json.dump({"results": all_jobs}, f, indent=4)

print("Raw data saved!")