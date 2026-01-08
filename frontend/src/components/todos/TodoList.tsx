'use client';

import { useEffect, useState } from 'react';
import { useAuth } from '@/components/CustomAuthProvider';
import { api } from '@/lib/api';
import TodoItem from './TodoItem'; // Import the TodoItem component

interface Task {
  id: number;
  title: string;
  description?: string;
  is_completed: boolean;
  priority?: string;
  created_at: string;
  updated_at: string;
  user_id: number;
}

export default function TodoList() {
  const [todos, setTodos] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [priority, setPriority] = useState('medium');
  const [editingId, setEditingId] = useState<number | null>(null);
  const { token } = useAuth(); // Get the auth token

  useEffect(() => {
    const fetchTodos = async () => {
      try {
        // Use the API client to fetch tasks
        const tasks = await api.getTasks();
        setTodos(tasks || []);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    if (token) { // Only fetch if we have a token
      fetchTodos();
    }
  }, [token]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim()) {
      alert('Title is required');
      return;
    }

    try {
      if (editingId !== null) {
        // Update existing task
        const updatedTask = await api.updateTask(editingId, {
          title,
          description,
          priority: priority.toLowerCase(), // Convert to lowercase to match backend enum
        });
        setTodos(todos.map(todo =>
          todo.id === editingId ? updatedTask : todo
        ));
      } else {
        // Create new task
        const newTask = await api.createTask({
          title,
          description,
          is_completed: false,
          priority: priority.toLowerCase(), // Convert to lowercase to match backend enum
        });
        setTodos([...todos, newTask]);
      }

      // Reset form
      setTitle('');
      setDescription('');
      setPriority('medium');
      setEditingId(null);
    } catch (error) {
      console.error('Error saving task:', error);
      alert('Error saving task');
    }
  };

  const handleEdit = (id: number) => {
    const task = todos.find(t => t.id === id);
    if (!task) return;
    setTitle(task.title);
    setDescription(task.description || '');
    setPriority(task.priority || 'medium');
    setEditingId(task.id);
  };

  const handleCancelEdit = () => {
    setTitle('');
    setDescription('');
    setPriority('medium');
    setEditingId(null);
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      try {
        await api.deleteTask(id);
        setTodos(todos.filter(todo => todo.id !== id));
      } catch (error) {
        console.error('Error deleting task:', error);
        alert('Error deleting task');
      }
    }
  };

  const handleToggle = async (id: number) => {
    try {
      // Find the task to get its current state
      const task = todos.find(t => t.id === id);
      if (!task) return;

      // Toggle the completion status
      const updatedTask = await api.updateTask(id, {
        is_completed: !task.is_completed
      });

      // Update the local state
      setTodos(todos.map(todo =>
        todo.id === id ? updatedTask : todo
      ));
    } catch (error) {
      console.error('Error toggling task completion:', error);
      alert('Error toggling task completion');
    }
  };

  if (loading) return <div>Loading todos...</div>;

  return (
    <div className="space-y-6">
      {/* Task Entry Form */}
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">
          {editingId !== null ? 'Edit Task' : 'Create New Task'}
        </h2>

        <div className="mb-4">
          <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-1">
            Title *
          </label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter task title"
            required
          />
        </div>

        <div className="mb-4">
          <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
            Description
          </label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Enter task description (optional)"
            rows={3}
          />
        </div>

        <div className="mb-4">
          <label htmlFor="priority" className="block text-sm font-medium text-gray-700 mb-1">
            Priority
          </label>
          <select
            id="priority"
            value={priority}
            onChange={(e) => setPriority(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </div>

        <div className="flex space-x-3">
          <button
            type="submit"
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            {editingId !== null ? 'Update Task' : 'Create Task'}
          </button>

          {editingId !== null && (
            <button
              type="button"
              onClick={handleCancelEdit}
              className="px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
            >
              Cancel
            </button>
          )}
        </div>
      </form>

      {/* Task List */}
      <div className="space-y-4">
        <h2 className="text-xl font-semibold">Your Tasks</h2>

        {todos.length === 0 ? (
          <p>No todos found. Create one to get started!</p>
        ) : (
          todos.map((todo) => (
            <TodoItem
              key={todo.id}
              id={todo.id}
              title={todo.title}
              description={todo.description}
              isCompleted={todo.is_completed}
              onToggle={handleToggle}
              onDelete={handleDelete}
              onEdit={() => handleEdit(todo.id)}
            />
          ))
        )}
      </div>
    </div>
  );
}
