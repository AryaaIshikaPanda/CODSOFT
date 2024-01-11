#To_Do_List
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully.")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\n1. Show tasks\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(new_task)
        elif choice == "3":
            try:
                task_index = int(input("Enter the task index to remove: "))
                remove_task(task_index)
            except ValueError:
                print("Invalid input for task index. Please enter a valid integer.")
        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

main()