#!/usr/bin/env python3
"""Main entry point for the In-Memory Console Todo Application"""

from app.todo.service import TodoService
from app.todo.presenter import TodoPresenter

def main():
    """Main application loop"""
    # Initialize components
    service = TodoService()
    presenter = TodoPresenter(service)

    # Display welcome message
    print("Welcome to the In-Memory Console Todo Application!")
    presenter.display_help()

    # Main loop
    while True:
        try:
            command = input("\nEnter command: ").strip()
            if not presenter.handle_command(command):
                break
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    main()