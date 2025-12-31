print("TODO List\n")

tasks = []  # Initialize the task list outside the loop

while True:
    print("1. Add Task")
    print("2. Finish Task")
    print("3. Save or Update Tasks")
    print("4. View Tasks")
    print("5. Exit\n")  # Option to exit the loop

    cmd = input("Enter your command: ")

    if cmd == "1":
        task_name = input("Enter task name: ")
        tasks.append(task_name)
        print(f"Task '{task_name}' added.\n")
    elif cmd == "2":
        task_name = input("Enter task name to delete: ")
        try:
            tasks.remove(task_name)
            print(f"Task '{task_name}' finished.\n")
        except ValueError:
            print("Task not found!\n")
    elif cmd == "3":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + '\n')
        print("Tasks saved to 'tasks.txt'.\n")
    elif cmd == "4":
        if tasks:
            print("Current Tasks:")
            for task in tasks:
                print(f"- {task}")
            print()  # New line for better readability
        else:
            print("No tasks available.\n")
    elif cmd == "5":
        print("Exiting the TODO list. Goodbye!")
        break
    else:
        print("Invalid command!\n")