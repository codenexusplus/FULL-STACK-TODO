'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { api } from '@/lib/api';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from '@/components/ui/select';
import { useAuth } from '@/components/CustomAuthProvider';

interface Task {
  id: number;
  title: string;
  description?: string;
  is_completed: boolean;
  priority: string;
  created_at: string;
  updated_at: string;
  user_id: number;
}

export default function TodosPage() {
  const { user, token, isAuthenticated } = useAuth();
  const router = useRouter();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [priority, setPriority] = useState('medium');
  const [editingId, setEditingId] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);

  // Redirect if not authenticated
  useEffect(() => {
    if (!isAuthenticated) {
      router.push('/');
    }
  }, [isAuthenticated, router]);

  // Fetch tasks when session is available and user ID exists and is not 0
  useEffect(() => {
    if (isAuthenticated && user && user.id && user.id !== 0) {
      fetchTasks();
    } else {
      setLoading(false); // Stop loading if user is not properly authenticated
    }
  }, [isAuthenticated, user]);

  const fetchTasks = async () => {
    try {
      const fetchedTasks = await api.getTasks();
      setTasks(fetchedTasks);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim()) return;

    try {
      if (editingId !== null) {
        // Update existing task
        const updatedTask = await api.updateTask(editingId, {
          title,
          description,
          priority: priority.toLowerCase(), // Convert to lowercase to match backend enum
        });

        // Update the task in the list
        setTasks(tasks.map(task =>
          task.id === editingId ? updatedTask : task
        ));

        // Reset editing state
        setEditingId(null);
      } else {
        // Create new task
        const newTaskObj = {
          title,
          description: description || '',
          is_completed: false,
          priority: priority.toLowerCase(), // Convert to lowercase to match backend enum
        };

        const createdTask = await api.createTask(newTaskObj);

        // Optimistic update
        setTasks([createdTask, ...tasks]);
      }

      // Reset form
      setTitle('');
      setDescription('');
      setPriority('medium');
    } catch (error) {
      console.error('Error saving task:', error);
    }
  };

  const onEdit = (task: Task) => {
    setTitle(task.title);
    setDescription(task.description || '');
    setPriority(task.priority || 'medium');
    setEditingId(task.id);
  };

  const cancelEdit = () => {
    setEditingId(null);
    setTitle('');
    setDescription('');
    setPriority('medium');
  };

  const toggleTaskCompletion = async (id: number) => {
    const task = tasks.find(t => t.id === id);
    if (!task) return;

    try {
      // Optimistic update
      const updatedTasks = tasks.map(t =>
        t.id === id ? { ...t, is_completed: !t.is_completed } : t
      );
      setTasks(updatedTasks);

      await api.updateTask(id, { is_completed: !task.is_completed });
    } catch (error) {
      console.error('Error updating task:', error);
      // Revert optimistic update on error
      fetchTasks();
    }
  };

  const deleteTask = async (id: number) => {
    const task = tasks.find(t => t.id === id);
    if (!task) return;

    try {
      // Optimistic update
      setTasks(tasks.filter(t => t.id !== id));

      await api.deleteTask(id);
    } catch (error) {
      console.error('Error deleting task:', error);
      // Revert optimistic update on error
      fetchTasks();
    }
  };

  if (!isAuthenticated || loading) {
    return <div className="flex justify-center items-center h-screen">Loading...</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8 text-center">Your Todo Dashboard</h1>

      <form onSubmit={handleSubmit} className="mb-8 p-6 bg-white rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">
          {editingId !== null ? 'Edit Task' : 'Add New Task'}
        </h2>

        <div className="mb-4">
          <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-1">
            Title *
          </label>
          <Input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Task title"
            className="w-full"
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
            Description
          </label>
          <Textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Task description (optional)"
            className="w-full"
            rows={3}
          />
        </div>

        <div className="mb-4">
          <label htmlFor="priority" className="block text-sm font-medium text-gray-700 mb-1">
            Priority
          </label>
          <Select value={priority} onValueChange={(value) => setPriority(value)}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select priority" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="high">High</SelectItem>
              <SelectItem value="medium">Medium</SelectItem>
              <SelectItem value="low">Low</SelectItem>
            </SelectContent>
          </Select>
        </div>

        <div className="flex gap-2">
          <Button type="submit">
            {editingId !== null ? 'Update Task' : 'Add Task'}
          </Button>

          {editingId !== null && (
            <Button type="button" variant="secondary" onClick={cancelEdit}>
              Cancel
            </Button>
          )}
        </div>
      </form>

      {tasks.length === 0 ? (
        <p className="text-center text-gray-500">No tasks yet. Add your first task above!</p>
      ) : (
        <ul className="space-y-4">
          {tasks.map((task) => (
            <li
              key={task.id}
              className={`flex flex-col p-4 bg-white rounded-lg shadow ${
                task.is_completed ? 'opacity-70' : ''
              }`}
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <input
                    type="checkbox"
                    checked={task.is_completed}
                    onChange={() => toggleTaskCompletion(task.id)}
                    className="mr-3 h-5 w-5"
                  />
                  <div>
                    <span className={`${task.is_completed ? 'line-through text-gray-500' : ''}`}>
                      {task.title}
                    </span>
                    <div className="text-xs text-gray-500 mt-1">
                      Priority: {task.priority?.toUpperCase() || 'MEDIUM'}
                    </div>
                  </div>
                </div>
                <div className="flex gap-2">
                  <Button
                    variant="outline"
                    size="sm"
                    onClick={() => onEdit(task)}
                  >
                    Edit
                  </Button>
                  <Button
                    variant="destructive"
                    size="sm"
                    onClick={() => deleteTask(task.id)}
                  >
                    Delete
                  </Button>
                </div>
              </div>

              {task.description && (
                <div className="mt-2 pl-8 text-gray-600">
                  {task.description}
                </div>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
