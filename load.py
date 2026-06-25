import pandas as pd
from sqlalchemy import create_engine

# Read cleaned CSV
df = pd.read_csv("clean/jobs_clean.csv")

# PostgreSQL connection
username = "postgres"
password = "9359392427"
host = "localhost"
port = "5432"
database = "job_market_db"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Load data into PostgreSQL
df.to_sql(
    "jobs",
    engine,
    if_exists="replace",   # replace table every run
    index=False
)

print("Data loaded successfully into PostgreSQL!")
print(f"Rows inserted: {len(df)}")