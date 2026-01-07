'use client';

import { createContext, useContext, useState, useEffect, ReactNode, useCallback } from 'react';
import { registerUser, loginUser, logoutUser } from '@/lib/auth-service';
import { toast } from 'react-hot-toast';

interface User {
  id: number;
  email: string;
  name: string;
  email_verified: boolean;
  is_active: boolean;
  image?: string;
  created_at: string;
}

interface AuthContextType {
  user: User | null;
  token: string | null;
  register: (email: string, password: string) => Promise<void>;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  isPending: boolean;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isPending, setIsPending] = useState(false);
  const [isInitialized, setIsInitialized] = useState(false);

  // Check for existing session on initial load
  useEffect(() => {
    const storedToken = localStorage.getItem('auth_token');
    const storedUser = localStorage.getItem('user');

    if (storedToken && storedUser) {
      try {
        setToken(storedToken);
        setUser(JSON.parse(storedUser));
      } catch (e) {
        console.error('Error parsing stored user data', e);
        // Clear invalid stored data
        localStorage.removeItem('auth_token');
        localStorage.removeItem('user');
      }
    }
    
    setIsInitialized(true);
  }, []);

  const login = useCallback(async (email: string, password: string) => {
    setIsPending(true);
    try {
      const response = await loginUser({ email, password });
      const { access_token } = response;

      // For this implementation, we'll store the token and a minimal user object
      // since the login response doesn't include user details
      const userResponse = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/auth/me`, {
        headers: {
          'Authorization': `Bearer ${access_token}`
        }
      });

      if (userResponse.ok) {
        const userData = await userResponse.json();
        setUser(userData);
        localStorage.setItem('user', JSON.stringify(userData));
      } else {
        // If we can't get user details, create a minimal user object
        const minimalUser = {
          id: 0, // Will be updated when we fetch user details
          email,
          name: email.split('@')[0],
          email_verified: false,
          is_active: true,
          created_at: new Date().toISOString()
        };
        setUser(minimalUser);
        localStorage.setItem('user', JSON.stringify(minimalUser));
      }

      setToken(access_token);
      localStorage.setItem('auth_token', access_token);
      toast.success('Login successful!');
    } catch (error: any) {
      console.error('Login error:', error);
      toast.error(error.message || 'Login failed');
      throw error;
    } finally {
      setIsPending(false);
    }
  }, []);

  const register = useCallback(async (email: string, password: string) => {
    setIsPending(true);
    try {
      const userData = await registerUser({ email, password });
      setUser(userData);
      localStorage.setItem('user', JSON.stringify(userData));
      
      // Automatically log in after registration
      await login(email, password);
      toast.success('Registration successful!');
    } catch (error: any) {
      console.error('Registration error:', error);
      toast.error(error.message || 'Registration failed');
      throw error;
    } finally {
      setIsPending(false);
    }
  }, [login]);

  const logout = useCallback(() => {
    setUser(null);
    setToken(null);
    localStorage.removeItem('auth_token');
    localStorage.removeItem('user');
    logoutUser();
    toast.success('Logged out successfully');
  }, []);

  const value = {
    user,
    token,
    register,
    login,
    logout,
    isPending,
    isAuthenticated: !!token && isInitialized
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}