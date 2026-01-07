import os

# Read the .env file directly to see its content
with open('.env', 'r') as f:
    content = f.read()
    print("Content of .env file:")
    print(content)
    print("\n---\n")

# Print the environment variables
print(f"DATABASE_URL from os.getenv: {os.getenv('DATABASE_URL')}")
print(f"API_SECRET_KEY from os.getenv: {os.getenv('API_SECRET_KEY')}")
print(f"BETTER_AUTH_SECRET from os.getenv: {os.getenv('BETTER_AUTH_SECRET')}")
print(f"BETTER_AUTH_URL from os.getenv: {os.getenv('BETTER_AUTH_URL')}")