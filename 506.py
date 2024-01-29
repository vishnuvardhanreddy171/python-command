import os
import pickle

class ToDoList:
    def __init__(self, filename='todolist.pkl'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added successfully.")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Display Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
