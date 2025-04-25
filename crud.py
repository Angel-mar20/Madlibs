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

    