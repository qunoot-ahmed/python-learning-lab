import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    tasks = load_tasks()
    task_title = input('Enter task title: ').strip().lower()
    task_completed = input('Enter task status: ').strip().lower()

    allowed_statuses = ["true", "false", "yes", "no"]

    if task_completed not in allowed_statuses:
        print("Task completed may either be true/yes or false/no")
        return

    task = {
        "title": task_title,
        "status": task_completed
    }
    tasks.append(task)
    save_tasks(tasks)
    print('Task added successfully.')


def view_tasks(tasks):
    if not tasks:
        print('No tasks found.')
        return

    for task in tasks:
        print(task)


def mark_task_complete():
    tasks = load_tasks()
    task_no = input('Enter task number: ')

    if not task_no.isdigit():
        print('Task number must be a numeric value.')

    task_index = int(task_no) - 1

    if task_index < 0 or task_index >= len(tasks):
        print('Invalid task number.')
        return

    tasks[task_index]["status"] = "yes"
    save_tasks(tasks)
    print("Task marked as complete.")


def delete_task():
    tasks = load_tasks()
    task_no = input('Enter task number to delete: ')

    if not task_no.isdigit():
        print('Task number must be a numeric value.')

    task_index = int(task_no) - 1

    if task_index < 0 or task_index >= len(tasks):
        print('Invalid task number.')
        return

    del tasks[task_index]
    save_tasks(tasks)
    print('Task deleted successfully.')
    return

def show_menu():
    print("\n===== Todo Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()

        elif choice == "2":
            tasks = load_tasks()
            view_tasks(tasks)

        elif choice == "3":
            mark_task_complete()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")

main()



