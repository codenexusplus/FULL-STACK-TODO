import os
from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv


class Settings(BaseSettings):
    database_url: str
    api_secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    better_auth_secret: str
    better_auth_url: str
    next_public_api_base_url: str = "http://localhost:8002"

    class Config:
        # Assuming the script runs from the 'backend' directory,
        # this will look for a .env file in that directory.
        env_file = ".env"
        env_file_encoding = 'utf-8'


# Create a single, cached settings instance.
settings = Settings()