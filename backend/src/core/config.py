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

    class Config:
        env_file = ".env"  # Use the standard pydantic-settings approach


# Load environment variables from the project root
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env_file_path = os.path.join(project_root, '.env')

# Load environment variables using python-dotenv
load_dotenv(dotenv_path=env_file_path)

# Create settings instance using environment variables
settings = Settings()