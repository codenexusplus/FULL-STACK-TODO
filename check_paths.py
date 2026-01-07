import os

# Check the actual project structure
current_file = os.path.abspath(__file__)
print(f"Current file: {current_file}")

# Check the project root path calculation in config.py
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(f"Project root calculated in config.py: {project_root}")

# Check if .env exists at the calculated path
env_file_path = os.path.join(project_root, '.env')
print(f"Expected .env path: {env_file_path}")
print(f"Does .env exist at that path? {os.path.exists(env_file_path)}")

# Check the actual current directory
print(f"Current working directory: {os.getcwd()}")

# Check if .env exists in the current directory
current_env_path = os.path.join(os.getcwd(), '.env')
print(f".env in current directory exists? {os.path.exists(current_env_path)}")