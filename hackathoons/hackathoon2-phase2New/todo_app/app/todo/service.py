# Service layer for todo operations

from typing import List, Optional
from .models import Todo

class TodoService:
    """Service class handling todo business logic"""

    def __init__(self):
        self._todos: List[Todo] = []
        self._next_id = 1

    def create(self, task: str) -> Todo:
        """Create a new todo item"""
        todo = Todo(id=self._next_id, task=task)
        self._todos.append(todo)
        self._next_id += 1
        return todo

    def get_all(self) -> List[Todo]:
        """Get all todo items"""
        return self._todos.copy()

    def get_by_id(self, id: int) -> Optional[Todo]:
        """Get a todo item by ID"""
        for todo in self._todos:
            if todo.id == id:
                return todo
        return None

    def update(self, id: int, task: str) -> Optional[Todo]:
        """Update a todo item"""
        todo = self.get_by_id(id)
        if todo:
            todo.task = task
            return todo
        return None

    def delete(self, id: int) -> bool:
        """Delete a todo item by ID"""
        todo = self.get_by_id(id)
        if todo:
            self._todos.remove(todo)
            return True
        return False

    def complete(self, id: int) -> bool:
        """Mark a todo as complete"""
        todo = self.get_by_id(id)
        if todo:
            todo.completed = True
            return True
        return False

    def clear(self) -> None:
        """Delete all todo items"""
        self._todos.clear()
        self._next_id = 1