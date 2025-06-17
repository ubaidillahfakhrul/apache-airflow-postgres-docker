# Airflow Weather Data Pipeline with PostgreSQL

This repository demonstrates an end-to-end data pipeline using **Apache Airflow**, extracting weather data from the **OpenWeatherMap API**, transforming it, and loading into a **PostgreSQL database**.

The pipeline is containerized using **Docker**, making it easy to deploy and run locally or in production environments.

---

## 🧩 Features

- ✅ Automated DAG for daily weather data extraction
- 🌤️ Integration with OpenWeatherMap API
- 🔁 Data transformation (Kelvin → Celsius)
- 💾 Data stored in PostgreSQL database
- 🐳 Fully containerized with Docker
- 📊 Ready for visualization or downstream processing

---

## 📁 Project Structure

---

## ⚙️ Prerequisites

- Docker & Docker Compose installed
- OpenWeatherMap API key ([https://openweathermap.org/api](https://openweathermap.org/api)) 
- Basic understanding of Apache Airflow and PostgreSQL

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ubaidillahfakhrul/apache-airflow-postgres-docker.git 
cd apache-airflow-postgres-docker
```
---

## ⚙️ Prerequisites

- Docker & Docker Compose installed
- OpenWeatherMap API key ([https://openweathermap.org/api](https://openweathermap.org/api)) 
- Basic understanding of Apache Airflow and PostgreSQL

---
### 2. Set your OpenWeatherMap API Key
Update the DAG file:
```bash
api_key = "YOUR_API_KEY"
```

### 3. Start the environment
```bash
docker-compose up -d
```










>
>
>
> ## 📚 Acknowledgements
> This project was inspired and based on the work from [mdh266](https://github.com/mdh266/AirflowDataPipeline).   
> The original repository demonstrates an ETL pipeline using Apache Airflow and PostgreSQL to extract weather data from OpenWeatherMap API.
>
> 🔗 Original Repository:  
> [https://github.com/mdh266/AirflowDataPipeline](https://github.com/mdh266/AirflowDataPipeline) 
>
> 📚 For a detailed explanation of how the DAG works, you can read the associated blog post from the original author.
> **Note**: This project is a modified version of the original, with additional features such as Docker support, custom logging, and enhanced error handling.
