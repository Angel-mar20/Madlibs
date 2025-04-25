import json
import os

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    