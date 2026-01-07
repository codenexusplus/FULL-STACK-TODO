import os
from dotenv import load_dotenv

# Load the .env file explicitly
load_dotenv('.env')

# Print the environment variables after loading
print(f"DATABASE_URL from os.getenv after loading .env: {os.getenv('DATABASE_URL')}")
print(f"API_SECRET_KEY from os.getenv after loading .env: {os.getenv('API_SECRET_KEY')}")
print(f"BETTER_AUTH_SECRET from os.getenv after loading .env: {os.getenv('BETTER_AUTH_SECRET')}")
print(f"BETTER_AUTH_URL from os.getenv after loading .env: {os.getenv('BETTER_AUTH_URL')}")