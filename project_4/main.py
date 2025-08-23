
tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"✅ '{task}' added to the list.")

    elif choice == "2":
        if not tasks:
            print("📌 No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("❌ No tasks to delete.")
        else:
            task_no = int(input("Enter task number to delete: "))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no-1)
                print(f"🗑️ Task '{removed}' deleted.")
            else:
                print("⚠ Invalid task number.")

    elif choice == "4":
        print("👋 Exiting... Have a productive day!")
        break

    else:
        print("⚠ Invalid choice, try again.")
