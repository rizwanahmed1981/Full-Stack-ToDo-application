# Presentation layer for console interface

from typing import List
from .models import Todo
from .service import TodoService

class TodoPresenter:
    """Presenter class handling console interface and user interaction"""

    def __init__(self, service: TodoService):
        self.service = service

    def display_todos(self, todos: List[Todo]) -> None:
        """Display all todos in a formatted way"""
        if not todos:
            print("No todos found.")
            return

        print(f"{'ID':<4} {'Status':<8} {'Task'}")
        print("-" * 50)
        for todo in todos:
            status = "Complete" if todo.completed else "Pending"
            print(f"{todo.id:<4} {status:<8} {todo.task}")

    def display_message(self, message: str) -> None:
        """Display a message to the user"""
        print(message)

    def display_help(self) -> None:
        """Display help information"""
        help_text = """
Available commands:
  add <task>         - Add a new todo
  list               - Display all todos
  complete <id>      - Mark a todo as complete
  update <id> <task> - Update an existing todo
  delete <id>        - Delete a todo
  clear              - Delete all todos
  help               - Show this help
  quit               - Exit the application
        """
        print(help_text.strip())

    def handle_command(self, command: str) -> bool:
        """Process a user command"""
        parts = command.strip().split()
        if not parts:
            return True

        cmd = parts[0].lower()

        try:
            if cmd == "add" and len(parts) > 1:
                task = " ".join(parts[1:])
                todo = self.service.create(task)
                self.display_message(f"Added todo: {todo.task}")

            elif cmd == "list":
                todos = self.service.get_all()
                self.display_todos(todos)

            elif cmd == "complete" and len(parts) > 1:
                try:
                    todo_id = int(parts[1])
                    if self.service.complete(todo_id):
                        self.display_message(f"Marked todo {todo_id} as complete")
                    else:
                        self.display_message(f"Todo with ID {todo_id} not found")
                except ValueError:
                    self.display_message("Invalid ID. Please provide a number.")

            elif cmd == "update" and len(parts) > 2:
                try:
                    todo_id = int(parts[1])
                    task = " ".join(parts[2:])
                    todo = self.service.update(todo_id, task)
                    if todo:
                        self.display_message(f"Updated todo {todo_id}: {todo.task}")
                    else:
                        self.display_message(f"Todo with ID {todo_id} not found")
                except ValueError:
                    self.display_message("Invalid ID. Please provide a number.")

            elif cmd == "delete" and len(parts) > 1:
                try:
                    todo_id = int(parts[1])
                    if self.service.delete(todo_id):
                        self.display_message(f"Deleted todo {todo_id}")
                    else:
                        self.display_message(f"Todo with ID {todo_id} not found")
                except ValueError:
                    self.display_message("Invalid ID. Please provide a number.")

            elif cmd == "clear":
                self.service.clear()
                self.display_message("All todos cleared")

            elif cmd == "help":
                self.display_help()

            elif cmd == "quit":
                return False

            else:
                self.display_message("Unknown command. Type 'help' for available commands.")

        except Exception as e:
            self.display_message(f"Error processing command: {str(e)}")

        return True