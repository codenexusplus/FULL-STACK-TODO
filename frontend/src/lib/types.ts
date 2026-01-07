export type Todo = {
  id: number;
  title: string;
  description?: string;
  is_completed: boolean;
  user_id: number;
  created_at: string;
  updated_at: string;
};

export type User = {
  id: number;
  email: string;
  created_at: string;
  updated_at: string;
};