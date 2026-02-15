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

Create a `.env` file in the project's root directory with your database and app settings, see `.env.example`

#### Create the database schema

To create the database:

```bash
cd scripts
PYTHONPATH=.. python3 init_db.py
```

> 💡 Ensure your `DATABASE_URL` is set properly before running these commands.

---

### Run the application

From the project root:

```bash
uvicorn app.main:app --reload
```

The application will be available at:  
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Swagger Docs at
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---
