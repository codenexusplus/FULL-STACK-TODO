import os

# Read the .env file line by line
with open('.env', 'r') as f:
    lines = f.readlines()

print("Lines in .env file:")
for i, line in enumerate(lines):
    print(f"{i+1}: {repr(line)}")

print("\nParsing DATABASE_URL manually:")
for line in lines:
    if line.startswith('DATABASE_URL='):
        db_url = line.split('=', 1)[1].strip()
        print(f"Found DATABASE_URL: {db_url}")
        break
else:
    print("DATABASE_URL not found in .env file")