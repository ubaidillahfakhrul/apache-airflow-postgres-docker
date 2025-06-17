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

