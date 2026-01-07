# Todo App with Authentication

A full-stack todo application with user authentication and authorization.

## Features

- User registration and login
- Secure todo management
- User-specific data isolation
- Responsive UI with toast notifications
- Type-safe API with validation

## Tech Stack

- **Backend**: Python, FastAPI, SQLModel, PostgreSQL
- **Frontend**: Next.js, TypeScript, Tailwind CSS
- **Authentication**: JWT-based authentication
- **Database**: PostgreSQL (with Neon)

## Setup Instructions

### Prerequisites

- Python 3.13+
- Node.js 18+
- PostgreSQL (or access to Neon DB)
- uv package manager

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

## API Documentation

See [API Documentation](./docs/api.md) for detailed API endpoints and usage.

## Architecture

The application follows a decoupled architecture with:

- A Python backend using FastAPI for API endpoints
- A PostgreSQL database for data persistence
- A Next.js frontend for the user interface
- JWT-based authentication for security
- Strict separation of concerns between frontend and backend