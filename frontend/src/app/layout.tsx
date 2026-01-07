import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import '../styles/globals.css';
import ToastProvider from '@/components/ToastProvider';
import { AuthProvider } from '@/components/CustomAuthProvider'; // Import the new provider

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Todo App',
  description: 'A full-stack todo application with authentication',
  icons: {
    icon: '/favicon.png',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          <ToastProvider>
          {children}
        </ToastProvider>
        </AuthProvider>
      </body>
    </html>
  );
}
