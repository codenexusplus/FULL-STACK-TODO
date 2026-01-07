# Quickstart Guide: Todo App with Authentication

## Prerequisites

- Python 3.13+
- Node.js 18+ 
- PostgreSQL (or access to Neon DB)
- uv package manager

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database connection details and other configurations
   ```

5. Run database migrations:
   ```bash
   python -m src.main init-db
   ```

6. Start the backend server:
   ```bash
   uv run dev
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your backend API URL and other configurations
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login an existing user

### Todo Management
- `GET /api/todos` - Get all todos for the authenticated user
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get a specific todo
- `PATCH /api/todos/{id}` - Update a specific todo
- `DELETE /api/todos/{id}` - Delete a specific todo

## Running Tests

### Backend Tests
```bash
# Run all backend tests
pytest

# Run tests with coverage
pytest --cov=src
```

### Frontend Tests
```bash
# Run all frontend tests
npm run test

# Run tests in watch mode
npm run test:watch
```

## Environment Variables

### Backend (.env)
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Secret key for JWT tokens
- `ALGORITHM` - Hashing algorithm for tokens
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time

### Frontend (.env)
- `NEXT_PUBLIC_API_URL` - Base URL for the backend API