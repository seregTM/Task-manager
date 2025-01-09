import json

def load_tasks(file_path="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, file_path="tasks.json"):
    """Save tasks to a JSON file."""
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {'Completed' if task['completed'] else 'Pending'}")

def add_task(tasks, title):
    """Add a new task."""
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")

def update_task(tasks, task_num):
    """Update the status of a task."""
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]
        print("Task status updated successfully!")
    else:
        print("Invalid task number.")

def delete_task(tasks, task_num):
    """Delete a task."""
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the Task Manager."""
    tasks = load_tasks()

    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("\nEnter the task title: ")
            add_task(tasks, title)
            save_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_num = int(input("\nEnter the task number to update: "))
                update_task(tasks, task_num)
                save_tasks(tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            display_tasks(tasks)
            try:
                task_num = int(input("\nEnter the task number to delete: "))
                delete_task(tasks, task_num)
                save_tasks(tasks)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
