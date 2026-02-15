import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable is required")

        self.MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
        if not self.MISTRAL_API_KEY:
            raise ValueError("MISTRAL_API_KEY environment variable is required")


# Instantiate a global settings object
settings = Settings()
