import datetime

tasks = []
habits = []

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Error: Task title cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    print(f"Task '{title}' added successfully!\n")

def list_tasks():
    if not tasks:
        print("No tasks added.\n")
        return
    print("Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{idx}. {task['title']} [{status}]")
    print()

def mark_task():
    try:
        num = int(input("Enter task number to mark as done: "))
        if num < 1 or num > len(tasks):
            raise IndexError("Task number out of range.")
        tasks[num-1]["done"] = True
        print(f"Marked '{tasks[num-1]['title']}' as done.\n")
    except ValueError:
        print("Error: Please enter a valid number.\n")
    except IndexError as e:
        print(f"Error: {e}\n")

def add_habit():
    name = input("Enter habit name: ").strip()
    if not name:
        print("Error: Habit name cannot be empty.")
        return
    frequency = input("Enter frequency (daily/weekly): ").strip().lower()
    if frequency not in ("daily", "weekly"):
        print("Error: Frequency must be 'daily' or 'weekly'.")
        return
    habits.append({
        "name": name,
        "frequency": frequency,
        "log": []
    })
    print(f"Habit '{name}' added as '{frequency}' habit!\n")

def list_habits():
    if not habits:
        print("No habits added.\n")
        return
    print("Habits:")
    for idx, habit in enumerate(habits, 1):
        print(f"{idx}. {habit['name']} ({habit['frequency']}) - {len(habit['log'])} times done")
    print()

def mark_habit():
    try:
        num = int(input("Enter habit number to mark as done: "))
        if num < 1 or num > len(habits):
            raise IndexError("Habit number out of range.")
        habits[num-1]["log"].append(datetime.date.today())
        print(f"Marked '{habits[num-1]['name']}' as done for today.\n")
    except ValueError:
        print("Error: Please enter a valid number.\n")
    except IndexError as e:
        print(f"Error: {e}\n")

def show_menu():
    print("CLI To-Do & Habit Tracker")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Add Habit")
    print("5. List Habits")
    print("6. Mark Habit as Done")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task()
        elif choice == "4":
            add_habit()
        elif choice == "5":
            list_habits()
        elif choice == "6":
            mark_habit()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid option. Please choose between 1 and 7.\n")

if __name__ == "__main__":
    main()
