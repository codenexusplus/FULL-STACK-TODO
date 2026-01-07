'use client';

import { Toaster } from 'react-hot-toast';
import { ReactNode } from 'react';

const ToastProvider = ({ children }: { children: ReactNode }) => {
  return (
    <>
      {children}
      <Toaster />
    </>
  );
};

export default ToastProvider;