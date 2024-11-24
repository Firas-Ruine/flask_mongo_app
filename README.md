# Mongo Flask Project

This project is a **Dockerized Flask application** integrated with **MongoDB**, designed for a modular, scalable architecture. The application supports data cleaning, insertion, and API routes for managing data.

---

## Features

- **Flask Framework:** Lightweight and modular backend.
- **MongoDB Integration:** Handles data storage with sharding and replication ready.
- **Data Cleaning:** Processes raw datasets before storing them in the database.
- **Dockerized Infrastructure:** Simplifies deployment and ensures consistency.
- **Modular Architecture:** Clear separation of routes, services, and utilities for maintainability.
- **Health Check API:** Quickly verify the application status.

---

## Project Structure

```
mongo_flask_project/
├── app/
│   ├── __init__.py            # Flask Application Factory
│   ├── routes/
│   │   ├── __init__.py        # Blueprint Initialization
│   │   ├── data_routes.py     # Routes for API Endpoints
│   │   ├── healthcheck.py     # Health Check Endpoints
│   ├── services/
│   │   ├── __init__.py        # Service Initialization
│   │   ├── data_service.py    # Business Logic for Data Operations
│   ├── models/
│   │   ├── __init__.py        # Models Initialization
│   │   ├── transaction_model.py # Transaction Schema (Optional, for validation)
│   ├── utils/
│   │   ├── __init__.py        # Utilities Initialization
│   │   ├── db.py              # MongoDB Connection
│   │   ├── data_cleaner.py    # Data Cleaning and Preprocessing Functions
│   ├── tests/
│   │   ├── test_routes.py     # Unit Tests for Routes
│   │   ├── test_services.py   # Unit Tests for Services
├── data/
│   ├── raw/                   # Raw Dataset Files
│   │   ├── data.csv           # Example CSV Dataset
│   ├── cleaned/               # Cleaned Dataset Files (Optional)
│       ├── cleaned_data.json
├── docker/
│   ├── mongodb/
│   │   ├── Dockerfile         # MongoDB Dockerfile
│   ├── flask/
│       ├── Dockerfile         # Flask Dockerfile
├── docker-compose.yml         # Docker Compose Configuration
├── requirements.txt           # Python Dependencies
├── .env                       # Environment Variables
├── README.md                  # Project Documentation
```

---

## Setup Instructions

### 1. Prerequisites
Ensure you have the following installed:
- **Docker**: [Install Docker](https://www.docker.com/get-started)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python (Optional)**: For local development.

---

### 2. Environment Variables

Create a `.env` file in the root directory with the following content:

```env
FLASK_ENV=development
MONGO_URI=mongodb://mongodb:27017/
DB_NAME=flask_db
```

---

### 3. Build and Run the Application

#### Using Docker Compose

1. **Build the Services**:
   ```bash
   docker-compose build
   ```

2. **Start the Containers**:
   ```bash
   docker-compose up
   ```

3. **Access the Application**:
   - **Flask App**: `http://localhost:5000`
   - **API Health Check**: `http://localhost:5000/api/health`
   - **Data Routes**: `http://localhost:5000/api/data/test`

4. **Stop the Containers**:
   ```bash
   docker-compose down
   ```

---

### 4. MongoDB Integration

You can access the MongoDB instance through a MongoDB client using the connection string:

```text
mongodb://localhost:27017/
```

---

### 5. Data Cleaning and Insertion

To clean and insert data from a raw dataset:

1. Place your dataset in the `data/raw/` directory (e.g., `data.csv`).
2. Trigger the data cleaning and insertion route:
   ```bash
   curl -X POST http://localhost:5000/api/data/insert
   ```

---

## Usage

### API Endpoints

| Method | Endpoint                  | Description                       |
|--------|---------------------------|-----------------------------------|
| GET    | `/api/health`             | Health check for the application |
| GET    | `/api/data/test`          | Test data route                  |
| POST   | `/api/data/insert`        | Clean and insert data into MongoDB |

---

## Development and Testing

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Flask Locally**:
   ```bash
   python run.py
   ```

3. **Run Tests**:
   Add unit tests in the `app/tests/` folder and run them using:
   ```bash
   pytest app/tests/
   ```

---

## Logs and Volumes

- Flask logs are stored in the `logs/` directory.
- MongoDB data is persisted using the `mongodb_data` volume.

