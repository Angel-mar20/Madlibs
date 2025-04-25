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

    def save_tasks(self):
        """Save tasks to a JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, title, description):
        """Add a new task."""
        new_task = Task(title, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully.")

    def view_tasks(self):
        """View all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task.completed else "✗"
            print(f"{index}. [{status}] {task.title}: {task.description}")

    def update_task(self, index, title=None, description=None):
        """Update an existing task."""
        try:
            task = self.tasks[index - 1]
            if title:
                task.title = title
            if description:
                task.description = description
            self.save_tasks()
            print(f"Task {index} updated successfully.")
        except IndexError:
            print("Error: Task index out of range.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_task(self, index):
        """Delete a task."""
        try:
            self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task {index} deleted successfully.")
        except IndexError:
            print("Error: Task index out of range.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Management Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            task_manager.update_task(index, title if title else None, description if description else None)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            task_manager.delete_task(index)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")



    
    