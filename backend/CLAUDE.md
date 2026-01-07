# Backend (FastAPI)

This directory contains the FastAPI backend application.

## Tech Stack

-   **Framework:** FastAPI
-   **Language:** Python
-   **ORM:** SQLModel
-   **Database:** Neon Serverless PostgreSQL
-   **Authentication:** JWT verification for tokens issued by Better Auth

## Development

To start the development server, run:

```bash
uvicorn src.main:app --reload
```

## Environment Variables

The backend requires the following environment variables to be set in a `.env` file:

-   `DATABASE_URL`: The connection string for the Neon PostgreSQL database.
-   `BETTER_AUTH_SECRET`: The secret key for verifying JWT signatures from Better Auth.
-   `API_SECRET_KEY`: A secret key for other API purposes.
