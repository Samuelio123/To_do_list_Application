import time

tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False, "start_time": time.time()})
    print("Task added!")

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for idx, task_info in enumerate(tasks, start=1):
            status = "Done" if task_info["done"] else "Not Done"
            task_time = " (Time: Completed)" if task_info["done"] else f" (Timer: {time_since(task_info['start_time'])})"
            print(f"{idx}. {task_info['task']} - {status}{task_time}")

def mark_task_done(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task removed!")
    else:
        print("Invalid task number.")

def time_since(start_time):
    elapsed_time = time.time() - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    return f"{minutes} min {seconds} sec"

while True:
    print("Options:")
    print("1. Add a new task")
    print("2. Display your tasks")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")

    choice = input("Please enter the number of your choice: ")

    if choice == "1":
        task = input("Enter the task description: ")
        add_task(task)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        task_number = int(input("Enter the number of the task to mark as done: "))
        mark_task_done(task_number)
    elif choice == "4":
        task_number = int(input("Enter the number of the task to remove: "))
        remove_task(task_number)
    elif choice == "5":
        print("Thank you for using the to-do list app. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

