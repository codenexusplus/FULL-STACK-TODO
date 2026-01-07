// Custom auth service to work with our backend API
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8002';

interface UserCredentials {
  email: string;
  password: string;
}

interface UserResponse {
  id: number;
  email: string;
  name: string;
  email_verified: boolean;
  is_active: boolean;
  image?: string;
  created_at: string;
}

interface LoginResponse {
  access_token: string;
  token_type: string;
}

export async function registerUser(credentials: UserCredentials): Promise<UserResponse> {
  const response = await fetch(`${API_BASE_URL}/api/auth/sign-up/email`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email: credentials.email,
      name: credentials.email.split('@')[0], // Use email prefix as name
      password: credentials.password,
    }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Registration failed');
  }

  return response.json();
}

export async function loginUser(credentials: UserCredentials): Promise<LoginResponse> {
  const formData = new FormData();
  formData.append('username', credentials.email);
  formData.append('password', credentials.password);

  const response = await fetch(`${API_BASE_URL}/api/auth/sign-in/email`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Login failed');
  }

  return response.json();
}

export async function logoutUser(): Promise<void> {
  // Get the token from localStorage
  const token = localStorage.getItem('auth_token');

  if (token) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/auth/sign-out`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        console.error('Logout failed:', response.status);
      }
    } catch (error) {
      console.error('Error during logout:', error);
    }
  }

  // Clear the client-side token
  console.log('User logged out');
}