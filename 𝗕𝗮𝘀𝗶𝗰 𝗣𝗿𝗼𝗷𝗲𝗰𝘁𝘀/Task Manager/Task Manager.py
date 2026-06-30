import json

# File to store tasks
FILENAME = "task.json"

# Load tasks from file if it exists
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

input("Press Enter to begin: ")

menu = '''\n---- Task Manager ----
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
'''

while True:
    tasks = load_tasks()  # always reload current tasks
    try:
        print(menu)
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        tasks[title] = description
        save_tasks(tasks)
        print("✅ Task added successfully!")

    elif choice == 2:
        print("\n📋 Your Tasks:")
        if not tasks:
            print("No tasks found. Please add some first.")
        else:
            for t, d in tasks.items():
                print(f"- {t}: {d}")

    elif choice == 3:
        if not tasks:
            print("No tasks available to update.")
        else:
            title = input("Enter task title you want to update: ")
            if title in tasks:
                print(f"Task '{title}' found.")
                new_desc = input("Enter new description: ")
                tasks[title] = new_desc
                save_tasks(tasks)
                print("✅ Task updated successfully!")
            else:
                print("❌ No task found with that title.")

    elif choice == 4:
        if not tasks:
            print("No tasks available to delete.")
        else:
            title = input("Enter task title to delete: ")
            if title in tasks:
                del tasks[title]
                save_tasks(tasks)
                print("✅ Task deleted successfully!")
            else:
                print("❌ No task found with that title.")

    elif choice == 5:
        print("👋 Exiting... Goodbye!")
        break  # cleaner than exit()

    else:
        print("❌ Invalid choice. Please enter a number between 1 and 5.")
