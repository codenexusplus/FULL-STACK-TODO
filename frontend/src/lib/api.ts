// frontend/src/lib/api.ts

interface TaskData {
  title: string;
  description?: string;
  is_completed: boolean;
  priority?: string;
}

interface Task extends TaskData {
  id: number;
  created_at: string;
  updated_at: string;
  user_id: number;
}

class ApiClient {
  private baseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8002';

  private async request(endpoint: string, options: RequestInit = {}) {
    const token = localStorage.getItem('auth_token'); // Get token from localStorage

    // Log a clear error if the JWT token is missing
    if (!token) {
      console.error('JWT token is missing from localStorage. Authentication will fail.');
    }

    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    } as Record<string, string>;

    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      ...options,
      headers,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  async getTasks(): Promise<Task[]> {
    // Get user ID from the stored user data
    const userData = localStorage.getItem('user');
    if (!userData) {
      throw new Error('User not authenticated');
    }

    const user = JSON.parse(userData);
    return this.request(`/api/todos/${user.id}/tasks`);
  }

  async createTask(taskData: Omit<TaskData, 'id' | 'user_id'>): Promise<Task> {
    // Get user ID from the stored user data
    const userData = localStorage.getItem('user');
    if (!userData) {
      throw new Error('User not authenticated');
    }

    const user = JSON.parse(userData);
    return this.request(`/api/todos/${user.id}/tasks`, {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  }

  async updateTask(taskId: number, taskData: Partial<TaskData>): Promise<Task> {
    // Get user ID from the stored user data
    const userData = localStorage.getItem('user');
    if (!userData) {
      throw new Error('User not authenticated');
    }

    const user = JSON.parse(userData);
    return this.request(`/api/todos/${user.id}/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(taskId: number): Promise<void> {
    // Get user ID from the stored user data
    const userData = localStorage.getItem('user');
    if (!userData) {
      throw new Error('User not authenticated');
    }

    const user = JSON.parse(userData);
    await this.request(`/api/todos/${user.id}/tasks/${taskId}`, {
      method: 'DELETE',
    });
  }
}

export const api = new ApiClient();