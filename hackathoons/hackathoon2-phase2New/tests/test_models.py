"""Tests for Todo models"""

import unittest
from app.todo.models import Todo

class TestTodoModel(unittest.TestCase):

    def test_todo_creation(self):
        """Test creating a todo"""
        todo = Todo(id=1, task="Test task")
        self.assertEqual(todo.id, 1)
        self.assertEqual(todo.task, "Test task")
        self.assertFalse(todo.completed)

    def test_todo_completion(self):
        """Test marking a todo as complete"""
        todo = Todo(id=1, task="Test task", completed=True)
        self.assertTrue(todo.completed)

if __name__ == '__main__':
    unittest.main()