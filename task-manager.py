import json

def load_tasks():
    """Load tasks from a JSON file."""
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['title']} - {'Completed' if task['completed'] else 'Pending'}")

def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter the task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added successfully!")

def update_task(tasks):
    """Update the status of a task."""
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = not tasks[task_num - 1]["completed"]
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task."""
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

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
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
