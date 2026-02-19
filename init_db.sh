#!/bin/bash
# Initialize database with pgvector extension

# This script runs as the PostgreSQL superuser
# Create the pgvector extension
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS vector;
EOSQL

echo "Database initialization completed successfully"
