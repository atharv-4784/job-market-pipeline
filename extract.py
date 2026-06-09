from dotenv import load_dotenv
import os
import requests

load_dotenv()

app_id = os.getenv("API_ID")
app_key = os.getenv("API_KEY")

if not app_id or not app_key:
    raise RuntimeError("API_ID and API_KEY must be set in the .env file")

url = "https://api.adzuna.com/v1/api/jobs/gb/search/1"
params = {
    "app_id": app_id,
    "app_key": app_key,
}


response = requests.get(url, params=params)

data = response.json()

print(response.status_code)
print(data["count"])

import json

with open("raw/jobs.json", "w") as f:
    json.dump(data, f, indent=4)

print("Raw data saved!")

