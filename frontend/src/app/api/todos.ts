// frontend/src/app/api/todos.ts
// This file contains utility functions for interacting with the todos API

import { Todo } from '@/lib/types';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

// Define the interface for API response
interface ApiResponse<T> {
  data?: T;
  message?: string;
  error?: string;
}

/**
 * Fetch all todos for the authenticated user
 */
export async function fetchTodos(token: string): Promise<ApiResponse<Todo[]>> {
  try {
    const response = await fetch(`${API_BASE_URL}/todos`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const todos = await response.json();
    return { data: todos };
  } catch (error) {
    console.error('Error fetching todos:', error);
    return { error: error instanceof Error ? error.message : 'Unknown error' };
  }
}

/**
 * Create a new todo
 */
export async function createTodo(token: string, todoData: Omit<Todo, 'id' | 'user_id' | 'created_at' | 'updated_at'>): Promise<ApiResponse<Todo>> {
  try {
    const response = await fetch(`${API_BASE_URL}/todos`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(todoData),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const newTodo = await response.json();
    return { data: newTodo };
  } catch (error) {
    console.error('Error creating todo:', error);
    return { error: error instanceof Error ? error.message : 'Unknown error' };
  }
}

/**
 * Update an existing todo
 */
export async function updateTodo(token: string, id: number, todoData: Partial<Todo>): Promise<ApiResponse<Todo>> {
  try {
    const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify(todoData),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const updatedTodo = await response.json();
    return { data: updatedTodo };
  } catch (error) {
    console.error('Error updating todo:', error);
    return { error: error instanceof Error ? error.message : 'Unknown error' };
  }
}

/**
 * Delete a todo
 */
export async function deleteTodo(token: string, id: number): Promise<ApiResponse<null>> {
  try {
    const response = await fetch(`${API_BASE_URL}/todos/${id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return { message: 'Todo deleted successfully' };
  } catch (error) {
    console.error('Error deleting todo:', error);
    return { error: error instanceof Error ? error.message : 'Unknown error' };
  }
}