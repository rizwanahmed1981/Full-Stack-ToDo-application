# In-Memory Console Todo Application

A Python 3.13 console-based todo application implementing CRUD operations with Clean Architecture principles.

## Features

- Create, Read, Update, Delete (CRUD) operations for todos
- Mark todos as complete
- Clean Architecture with separation of concerns:
  - Presentation Layer: Console interface
  - Service Layer: Business logic
  - Data Layer: In-memory storage

## Installation

1. Make sure you have Python 3.12 or higher installed
2. Navigate to the project directory
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Available Commands
- `add <task>` - Add a new todo item
- `list` - Display all todos
- `complete <id>` - Mark a todo as complete
- `update <id> <new_task>` - Update an existing todo
- `delete <id>` - Delete a todo
- `clear` - Delete all todos
- `help` - Show available commands
- `quit` - Exit the application

## Project Structure

```
todo_app/
├── main.py                 # Entry point
├── app/
│   ├── __init__.py
│   └── todo/
│       ├── __init__.py
│       ├── models.py       # Todo model definitions
│       ├── service.py      # Business logic and todo operations
│       └── presenter.py    # Console interface and user interaction
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_service.py
    └── test_presenter.py
```

## Architecture

The application follows Clean Architecture principles:
1. **Presentation Layer**: Handles user interaction via console interface
2. **Service Layer**: Contains business logic and manages todo operations
3. **Data Layer**: Implements in-memory storage for todos

## Testing

Run tests with:
```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.