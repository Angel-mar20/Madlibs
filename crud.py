import json
import os

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True
    
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = [Task(**task) for task in json.load(file)]
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading tasks: {e}")

    