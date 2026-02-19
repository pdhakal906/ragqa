# ragqa-backend

This project is a **FastAPI** application using **Postgres** as the database.

## Docker Setup

### Prerequisites for Docker

- Docker Engine
- Docker Compose

### Setup with Docker

#### 1. Configure environment variables

Create `.env` file and add variables just like in `.env.example`

#### 2. Build and Start the Application

```bash
docker compose up --build
```

#### 3. Access the Application

Once the containers are running:

- **API Swagger Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

#### 4. Useful Docker Commands

Stop the application:

```bash
docker compose down
```

Restart services:

```bash
docker compose restart
```

Access PostgreSQL inside a container:

```bash
docker compose exec postgres psql -U raguser -d ragdb
```

#### 5. Database Migrations

Migrations are automatically run when the application starts. If you need to run them manually:

```bash
docker compose exec app alembic upgrade head
```

## Local Setup (Alternative)

Before you begin, make sure you have the following installed:

- Python 3.12 or later
- PostgreSQL
- Virtual environment tools (`venv`)
- `pip` package manager

## Setup Instructions

### 1. Clone the repository

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Create a datbase for example: `ragdb` from psql

```bash
//open postgres
sudo -i -u postgres

//open psql
psql

CREATE DATABASE ragdb;

```

Inside the same psql check if you have pgvector installed:

SELECT version();

You’ll see something like:

PostgreSQL 16.x on x86_64-pc-linux-gnu

Remember the version number (e.g., 14, 15, 16).

Install pgvector for Your Version

On Linux:

```bash
sudo apt update
sudo apt install postgresql-server-dev-16
sudo apt install postgresql-16-pgvector
```

Replace 16 with your actual PostgreSQL version.

Example if using 15:

```bash
sudo apt install postgresql-server-dev-15
sudo apt install postgresql-15-pgvector
```

Back inside psql:

```bash
CREATE EXTENSION IF NOT EXISTS vector;
```

### 5. Configure environment variables

Create a `.env` file in the project's root directory, see `.env.example`

### 6. Run migration

From the project root:

```bash

aelmbic upgrade head

```

### Run the application

From the project root:

```bash
uvicorn app.main:app --reload
```

Swagger Docs at
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Booting up the application usually takes a bit time as the sententence transformer `BAAI/bge-small-en-v1.5` is downloaded each time.

---
