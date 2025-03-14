# Automated ETL Pipeline for Multi-Platform Restaurant Booking Data Integration and Analytics

## Project Overview

This project automates the management of restaurant bookings through a robust ETL pipeline orchestrated by Apache Airflow.   
It simulates data flows from multiple restaurant booking services using custom-built APIs that closely resemble real-world endpoints. 
For example, the system includes simulated APIs representing data structures and responses from popular platforms such as TheFork, Quandoo, OpenTable, and SevenRooms.
The system extracts reservation data from **API endpoints**, standardizes it, and stores it in a **PostgreSQL** database for centralized tracking. 
A **Tableau Dashboard** provides insights into booking trends, occupancy rates, and platform performance.

Additionally, this project includes **FindTables**, a **Django-based restaurant booking system** that simulates real-world table reservations. Users can make and manage reservations through API endpoints and a **frontend**.

<div align="center">
  <img src="https://github.com/user-attachments/assets/98eb1307-1f0a-4461-9231-c99e174b46ae" alt="Project Image">
</div>

---

## Features

**Automated ETL Pipeline** – Extracts, transforms, and loads booking data from multiple platforms.  
**Centralized Database** – Stores structured reservation data in **PostgreSQL/MySQL**.  
**Data Standardization** – Ensures uniformity in booking data across platforms.  
**Interactive Dashboard** – Analyzes booking trends, occupancy rates, and platform performance.  
**Django-Based Booking System** – Simulates restaurant reservations via API endpoints.  
**Webhook Simulation** – Simulates real-time booking updates from platforms.  
**Cloud-Ready Architecture** – Can be deployed on **AWS, Docker, or local environments**.  

---

## Project Structure

```
📂 restaurant-booking-management  
│── 📂 dags/                   # Apache Airflow DAGs for ETL workflows
│── 📂 dags/helpers            # Data extraction & transformation scripts    
│── 📂 FindTables/             # Django-based FindTables booking system  
│── 📂 queries/                # PostgreSQL schema and scripts  
│── 📂 dashboards/             # Tableau dashboard files  
│── 📜 README.md                  # Project documentation  

```

---

## Tech Stack

| Component           | Technology Used |
|---------------------|----------------|
| **Orchestration**  | Apache Airflow  |
| **Backend**        | Django & DRF |
| **Database**       | PostgreSQL|
| **Data Processing** | Pydantic, Pandas, Python |
| **Visualization**  | Tableau |
| **Frontend**       | jQuery, HTML, CSS |
| **Deployment**     | Docker, AWS |

---

## How It Works

### Extract Booking Data
- Airflow DAGs receives **reservation data** from custom built webhooks in Django.
- Data is fetched in different formats (JSON, CSV) and standardized.

### Transform & Standardize
- Python scripts clean, validate, and standardize booking data.
- Ensures uniformity across seperate databases. 

### Load into Database
- Standardized data is stored in **PostgreSQL**.
- Enables **efficient querying** and integration with the dashboard.

### Dashboard Analysis
- Tableau visualizes:
  - **Booking trends** across platforms
  - **Occupancy rates** per restaurant
  - **Platform performance** comparisons

### FindTables - Django-Based Booking System
- Allows users to **simulate restaurant bookings** via API.
- Stores bookings in the central database.

### Webhook Simulation
- Simulates real-time booking updates from different platforms.
- Updates database whenever a **reservation is modified or canceled**.

## 📜 License
This project is licensed under the **MIT License**.

---

## 📩 Contact & Contributions
- **Author:** Paritosh   
- **Contributions:** PRs are welcome! Open an issue for suggestions.  
