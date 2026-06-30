# 📊 Job Market Analytics Pipeline

An end-to-end **ETL (Extract, Transform, Load)** pipeline that collects live UK job listings from the **Adzuna API**, cleans and transforms the data using **Python**, stores it in **PostgreSQL**, and presents actionable insights through interactive **Power BI dashboards**.

---

## 🚀 Features

- 🔍 Extracts live job listings from the Adzuna API
- 🧹 Cleans and transforms raw JSON data
- ❌ Removes duplicate records
- 📌 Handles missing values
- 💰 Calculates average salaries
- ⏱️ Differentiates hourly and annual salary records
- 🗄️ Loads processed data into PostgreSQL
- 📈 Builds interactive Power BI dashboards
- ⚡ Supports automated ETL execution

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Processing | Pandas |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Visualization | Power BI |
| API | Adzuna REST API |
| Version Control | Git, GitHub |

---

## 📂 Project Structure

```text
JOB_MARKET_PIPELINE/
│
├── raw/
│   └── jobs.json
│
├── clean/
│   └── jobs_clean.csv
│
├── sql/
│   ├── schema.sql
│   ├── create_tables.sql
│   └── analytics_queries.sql
│
├── dashboard/
│   ├── job_pipeline_Dashboard.pbix
│   ├── Overview.png
│   └── Salary Analysis.png
│
├── Screenshots/
│   ├── Overview.png
│   ├── Salary Analysis.png
│   └── Pipeline.png
│
├── extract.py
├── transform.py
├── load.py
├── Auto_pipeline.py
├── test_s3.py
├── explore.ipynb
│
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── anaconda_projects/
├── __pycache__/
├── .ipynb_checkpoints/
└── venv/
```

---

# 🔄 ETL Pipeline

<p align="center">
  <img src="Screenshots/Pipeline.png" width="900">
</p>

---

# 📊 Power BI Dashboards

## Executive Overview

<p align="center">
  <img src="dashboard/Overview.png" width="900">
</p>

### Highlights

- Total Jobs
- Total Companies
- Total Locations
- Average Salary
- Top Hiring Companies
- Job Distribution by Category

---

## Salary Analysis

<p align="center">
  <img src="dashboard/Salary%20Analysis.png" width="900">
</p>

### Highlights

- Highest Paying Roles
- Salary Distribution
- Average Salary by Category
- Top Paying Companies
- Salary Comparison Across Locations

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/JOB_MARKET_PIPELINE.git
```

Navigate to the project

```bash
cd JOB_MARKET_PIPELINE
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure environment variables

Create a `.env` file and add:

```env
APP_ID=your_adzuna_app_id
APP_KEY=your_adzuna_app_key

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

# ▶️ Running the Pipeline

### Step 1 – Extract Data

```bash
python extract.py
```

### Step 2 – Transform Data

```bash
python transform.py
```

### Step 3 – Load Data

```bash
python load.py
```

### Step 4 – Run Complete ETL Pipeline

```bash
python Auto_pipeline.py
```

---

# 📈 Key Insights

The dashboard provides insights into:

- 📍 Hiring trends across UK locations
- 🏢 Top hiring companies
- 💼 Most in-demand job titles
- 💰 Salary distribution
- 📊 Average salaries by category
- ⭐ Highest paying roles

---

# 🔮 Future Improvements

- Docker support
- Scheduled ETL using Airflow
- AWS S3 integration
- CI/CD with GitHub Actions
- Interactive web dashboard using Streamlit

---

# 👨‍💻 Author

**Atharv Bhore**

- GitHub: https://github.com/atharv-4784
- LinkedIn: https://linkedin.com/in/atharv-bhore

---

⭐ If you found this project useful, consider giving it a star.