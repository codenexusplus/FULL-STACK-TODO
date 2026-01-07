'use client';

import { Button } from '@/components/ui/button';
import { useRouter } from 'next/navigation';
import Link from 'next/link';

export function Header() {
  const router = useRouter();
  
  const handleLogout = () => {
    localStorage.removeItem('token');
    router.push('/');
  };

  const token = localStorage.getItem('token');
  
  return (
    <header className="bg-white shadow-sm">
      <div className="container mx-auto px-4 py-4 flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold text-indigo-700">
          TodoApp
        </Link>
        
        <nav>
          {token ? (
            <div className="flex items-center space-x-4">
              <Link href="/dashboard" className="text-gray-600 hover:text-indigo-600">
                Dashboard
              </Link>
              <Button variant="outline" onClick={handleLogout}>
                Logout
              </Button>
            </div>
          ) : (
            <div className="flex space-x-4">
              <Link href="/login">
                <Button variant="outline">Login</Button>
              </Link>
              <Link href="/register">
                <Button>Sign Up</Button>
              </Link>
            </div>
          )}
        </nav>
      </div>
    </header>
  );
}