import pickle
import datetime

def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return []

def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as file:
        pickle.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else " "
            print(f"{idx}. [{status}] {task['title']} - Due: {task['due_date']}")

def sort_tasks_by_due_date(tasks):
    return sorted(tasks, key=lambda x: x['due_date'])

def filter_tasks_by_status(tasks, completed):
    return [task for task in tasks if task['completed'] == completed]

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Edit Task")
        print("4. Display Tasks")
        print("5. Display Completed Tasks")
        print("6. Display Incomplete Tasks")
        print("7. Sort Tasks by Due Date")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
                tasks.append({'title': title, 'due_date': due_date, 'completed': False})
                save_tasks(tasks)
                print("Task added successfully!")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == '2':
            display_tasks(tasks)
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]['completed'] = True
                save_tasks(tasks)
                print("Task marked as complete!")

        elif choice == '3':
            display_tasks(tasks)
            task_number = int(input("Enter the task number to edit: ")) - 1
            if 0 <= task_number < len(tasks):
                new_title = input("Enter new task title: ")
                tasks[task_number]['title'] = new_title
                new_due_date_str = input("Enter new due date (YYYY-MM-DD): ")
                try:
                    new_due_date = datetime.datetime.strptime(new_due_date_str, '%Y-%m-%d').date()
                    tasks[task_number]['due_date'] = new_due_date
                    save_tasks(tasks)
                    print("Task edited successfully!")
                except ValueError:
                    print("Invalid date format. Task not edited.")

        elif choice == '4':
            display_tasks(tasks)

        elif choice == '5':
            completed_tasks = filter_tasks_by_status(tasks, True)
            display_tasks(completed_tasks)

        elif choice == '6':
            incomplete_tasks = filter_tasks_by_status(tasks, False)
            display_tasks(incomplete_tasks)

        elif choice == '7':
            sorted_tasks = sort_tasks_by_due_date(tasks)
            display_tasks(sorted_tasks)

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
