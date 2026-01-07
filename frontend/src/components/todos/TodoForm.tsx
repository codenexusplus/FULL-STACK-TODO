// frontend/src/components/todos/TodoForm.tsx
import React, { useState } from 'react';
import { Todo } from '@/lib/types';

interface TodoFormProps {
  todo?: Todo;
  onSave: (todo: Omit<Todo, 'id' | 'user_id' | 'created_at' | 'updated_at'> | Partial<Todo>) => void;
  onCancel: () => void;
}

const TodoForm: React.FC<TodoFormProps> = ({ todo, onSave, onCancel }) => {
  const [title, setTitle] = useState(todo?.title || '');
  const [description, setDescription] = useState(todo?.description || '');
  const [isCompleted, setIsCompleted] = useState(todo?.is_completed || false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim()) {
      alert('Title is required');
      return;
    }

    if (todo) {
      // Update existing todo
      onSave({
        title: title.trim(),
        description: description.trim(),
        is_completed: isCompleted
      });
    } else {
      // Create new todo
      onSave({
        title: title.trim(),
        description: description.trim(),
        is_completed: isCompleted
      });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4 p-4 border rounded-lg bg-gray-50">
      <div className="mb-3">
        <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-1">
          Title *
        </label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
          placeholder="Enter todo title"
          required
        />
      </div>

      <div className="mb-3">
        <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
          Description
        </label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
          placeholder="Enter todo description (optional)"
          rows={3}
        />
      </div>

      <div className="mb-4 flex items-center">
        <input
          type="checkbox"
          id="isCompleted"
          checked={isCompleted}
          onChange={(e) => setIsCompleted(e.target.checked)}
          className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
        />
        <label htmlFor="isCompleted" className="ml-2 block text-sm text-gray-700">
          Mark as completed
        </label>
      </div>

      <div className="flex space-x-2">
        <button
          type="submit"
          className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          {todo ? 'Update Todo' : 'Add Todo'}
        </button>
        <button
          type="button"
          onClick={onCancel}
          className="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Cancel
        </button>
      </div>
    </form>
  );
};

export default TodoForm;