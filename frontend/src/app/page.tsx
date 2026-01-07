'use client';

import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { useRouter } from 'next/navigation';

export default function HomePage() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const router = useRouter();

  useEffect(() => {
    // Check if JWT token exists in localStorage
    const token = localStorage.getItem('token');
    if (token) {
      setIsLoggedIn(true);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    setIsLoggedIn(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <header className="flex justify-between items-center py-6">
          <h1 className="text-3xl font-bold text-indigo-700">TodoApp</h1>
          {isLoggedIn ? (
            <Button 
              variant="outline" 
              onClick={handleLogout}
              className="text-indigo-600 border-indigo-600 hover:bg-indigo-50"
            >
              Logout
            </Button>
          ) : null}
        </header>

        <main className="flex flex-col items-center justify-center py-20">
          <div className="text-center max-w-2xl">
            <h1 className="text-5xl font-bold text-gray-800 mb-6">
              Welcome to Your <span className="text-indigo-600">Todo App</span>
            </h1>
            <p className="text-xl text-gray-600 mb-10">
              Organize your tasks, boost productivity, and achieve your goals with our intuitive todo application.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              {isLoggedIn ? (
                <Button
                  size="lg"
                  className="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-6 text-lg"
                  onClick={() => router.push('/dashboard')}
                >
                  Go to Dashboard
                </Button>
              ) : (
                <>
                  <Button 
                    size="lg" 
                    variant="outline" 
                    className="border-indigo-600 text-indigo-600 hover:bg-indigo-50 px-8 py-6 text-lg"
                    onClick={() => router.push('/login')}
                  >
                    Login
                  </Button>
                  <Button 
                    size="lg" 
                    className="bg-indigo-600 hover:bg-indigo-700 text-white px-8 py-6 text-lg"
                    onClick={() => router.push('/register')}
                  >
                    Sign Up
                  </Button>
                </>
              )}
            </div>
          </div>
        </main>

        <footer className="py-8 text-center text-gray-500">
          <p>© {new Date().getFullYear()} TodoApp. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
}