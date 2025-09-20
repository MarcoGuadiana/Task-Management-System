# Import functions from task_manager.task_utils package
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def main():
    """The main function to run the task management system."""
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (MM-DD-YEAR): ")
            add_task(title, description, due_date)
            
        elif choice == "2":
            try:
                index = int(input("Enter the index of the task to mark as complete: ")) - 1
                mark_task_as_complete(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif choice == "3":
            view_pending_tasks()
            
        elif choice == "4":
            progress = calculate_progress()
            print(f"Your progress: {progress:.2f}% completed.")
            
        elif choice == "5":
            print("Exiting the program... Thanks for using us comeback again!")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()