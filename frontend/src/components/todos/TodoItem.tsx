'use client';

import { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import { Trash2, Edit3 } from 'lucide-react';

interface TodoItemProps {
  id: number;
  title: string;
  description?: string;
  isCompleted: boolean;
  priority?: string;
  onToggle: (id: number) => void;
  onDelete: (id: number) => void;
  onEdit?: (id: number) => void;
}

export default function TodoItem({
  id,
  title,
  description,
  isCompleted,
  priority,
  onToggle,
  onDelete,
  onEdit
}: TodoItemProps) {
  const [isChecked, setIsChecked] = useState(isCompleted);

  // Update local state when parent changes the isCompleted prop
  useEffect(() => {
    setIsChecked(isCompleted);
  }, [isCompleted]);

  const handleToggle = () => {
    const newCheckedState = !isChecked;
    setIsChecked(newCheckedState);
    onToggle(id);
  };

  const handleDelete = () => {
    onDelete(id);
  };

  const handleEdit = () => {
    if (onEdit) {
      onEdit(id);
    }
  };

  // Determine priority display and styling
  const priorityDisplay = priority ? priority.toUpperCase() : 'MEDIUM';
  const priorityColor = priority === 'high' ? 'text-red-500' :
                       priority === 'medium' ? 'text-yellow-500' :
                       priority === 'low' ? 'text-green-500' : 'text-gray-500';

  return (
    <div className={`flex flex-col p-4 border rounded-lg ${isChecked ? 'bg-gray-100' : 'bg-white'}`}>
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3 flex-1">
          <Checkbox
            checked={isChecked}
            onCheckedChange={handleToggle}
            className="data-[state=checked]:bg-blue-500"
          />
          <div className="flex-1">
            <h3 className={`font-medium ${isChecked ? 'line-through text-gray-500' : 'text-gray-900'}`}>
              {title}
            </h3>
            <p className={`text-xs ${priorityColor} mt-1`}>
              Priority: {priorityDisplay}
            </p>
          </div>
        </div>
        <div className="flex space-x-1">
          {onEdit && (
            <Button
              variant="ghost"
              size="sm"
              onClick={handleEdit}
              className="text-blue-500 hover:text-blue-700"
            >
              <Edit3 className="h-4 w-4" />
            </Button>
          )}
          <Button
            variant="ghost"
            size="sm"
            onClick={handleDelete}
            className="text-red-500 hover:text-red-700"
          >
            <Trash2 className="h-4 w-4" />
          </Button>
        </div>
      </div>
      {description && (
        <div className={`mt-2 pl-8 text-sm ${isChecked ? 'line-through text-gray-400' : 'text-gray-600'}`}>
          {description}
        </div>
      )}
    </div>
  );
}