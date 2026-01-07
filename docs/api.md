# Todo App API Documentation

## Overview

The Todo App API provides endpoints for managing todo items with user authentication and authorization. Each todo item is associated with a specific user, ensuring data privacy and ownership.

## Authentication

All API endpoints (except authentication endpoints) require a valid JWT token in the Authorization header:

```
Authorization: Bearer <jwt_token>
```

## Endpoints

### Authentication

#### POST /api/auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

#### POST /api/auth/login
Log in an existing user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

### Todo Management

#### GET /api/todos
Retrieve all todos for the authenticated user.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample Todo",
    "description": "A sample todo item",
    "is_completed": false,
    "user_id": 1,
    "created_at": "2023-01-01T00:00:00",
    "updated_at": "2023-01-01T00:00:00"
  }
]
```

#### POST /api/todos
Create a new todo for the authenticated user.

**Request Body:**
```json
{
  "title": "New Todo",
  "description": "Description of the new todo",
  "is_completed": false
}
```

**Response:**
```json
{
  "id": 2,
  "title": "New Todo",
  "description": "Description of the new todo",
  "is_completed": false,
  "user_id": 1,
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00"
}
```

#### GET /api/todos/{id}
Retrieve a specific todo by ID for the authenticated user.

**Response:**
```json
{
  "id": 1,
  "title": "Sample Todo",
  "description": "A sample todo item",
  "is_completed": false,
  "user_id": 1,
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00"
}
```

#### PATCH /api/todos/{id}
Update a specific todo by ID for the authenticated user.

**Request Body:**
```json
{
  "title": "Updated Todo",
  "description": "Updated description",
  "is_completed": true
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Updated Todo",
  "description": "Updated description",
  "is_completed": true,
  "user_id": 1,
  "created_at": "2023-01-01T00:00:00",
  "updated_at": "2023-01-01T00:00:00"
}
```

#### DELETE /api/todos/{id}
Delete a specific todo by ID for the authenticated user.

**Response:**
```json
{
  "message": "Todo deleted successfully"
}
```