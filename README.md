# ragqa-backend

This project is a **FastAPI** application using **Postgres** as the database.

## Prerequisites

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

### 4. Configure environment variables

Create a `.env` file in the project's root directory, see `.env.example`

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

#### Create the database schema

To create the database:

```bash
cd scripts
PYTHONPATH=.. python3 init_db.py
```

Ensure your `DATABASE_URL` is set properly before running these commands.

---

### Run the application

From the project root:

```bash
uvicorn app.main:app --reload
```

Swagger Docs at
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---
