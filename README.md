# 🧊 ELT Pipeline: API + MySQL to S3 → Snowflake → dbt

A modern ELT pipeline that:
- Extracts data from a public API (CoinGecko) and optionally from MySQL
- Loads the raw data into Amazon S3 as cost-optimized Parquet files
- Ingests data into Snowflake using `COPY INTO`
- Transforms data inside Snowflake using `dbt`
- Schedules the pipeline using Apache Airflow

---

## 📌 Features

- ✅ **ELT architecture**: fast, cloud-optimized data pipeline  
- 🪙 **CoinGecko API integration**: sample extract of real-time crypto prices  
- 💾 **S3 Storage**: compressed Parquet format to minimize cost  
- ❄️ **Snowflake DWH**: scalable cloud-based analytics platform  
- 🔁 **Airflow DAG**: automates daily scheduling  
- 📊 **dbt models**: modular SQL transformations for analytics  

---

## 📁 Project Structure

```
elt_pipeline/
│
├── dags/                         # Airflow DAG for scheduling
│   └── elt_crypto_pipeline.py
├── extract/                      # Extraction scripts
│   └── extract_coingecko.py
├── load/                         # Load scripts to S3
│   └── load_to_s3.py
├── ingest/                       # Ingest data from S3 to Snowflake
│   └── snowflake_ingest.py
├── dbt_project/                  # dbt transformations
│   └── models/
│       └── transform_crypto.sql
└── requirements.txt              # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. 🔧 Environment Setup

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install and start Apache Airflow (example for local environment):

```bash
export AIRFLOW_HOME=~/airflow
airflow db init
airflow webserver --port 8080
airflow scheduler
```

### 2. 🔐 Configuration

Set your credentials for:

- AWS S3 (bucket, access keys, region)
- Snowflake (user, password, account, integration name)
- MySQL (optional)

Update the following scripts with your credentials:
- `load_to_s3.py`
- `elt_crypto_pipeline.py`

### 3. 🛰️ Run the Pipeline

In Airflow UI:
- Enable the `elt_crypto_pipeline` DAG
- Trigger manually or wait for scheduled run

---

## 🧪 Optional: Run dbt Transformations

```bash
cd dbt_project
dbt init
dbt run
```

---

## 💰 S3 Cost Optimization

- Files are saved in **Parquet format** with **Snappy compression**
- Organize S3 keys by date prefix to enable partition pruning
- Optionally set **S3 lifecycle rules** to transition old data to Glacier

---

## 🚀 Future Extensions

- Add **MySQL** data extraction module
- Implement **Great Expectations** for data quality checks
- Add **Superset or Looker** for BI dashboards
- Use **AWS Lambda** + **Snowpipe** for real-time ingestion

---

## 🧑‍💻 Author

Maurice Oboya  
[GitHub](https://github.com/mauriceoboya)

---

## 📄 License

This project is licensed under the MIT License.
