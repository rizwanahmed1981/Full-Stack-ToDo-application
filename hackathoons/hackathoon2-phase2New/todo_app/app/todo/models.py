# Todo model definition

from dataclasses import dataclass
from typing import Optional

@dataclass
class Todo:
    """Data class representing a todo item"""
    id: int
    task: str
    completed: bool = False