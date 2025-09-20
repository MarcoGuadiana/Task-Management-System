from datetime import datetime

# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not (validate_task_title(title) and 
            validate_task_description(description) and 
            validate_due_date(due_date)):
        return False
    
    task =  {
        "title": title.strip(),
        "description":description.strip(),
        "due_date": due_date.strip(), 
        "completed": False
    }
    tasks.append(task)
    None
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index):
    
    try:
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Error: Invalid task index.")
    except (TypeError, IndexError):
        print("Error: Invalid input for task index.")

# Implement view_pending_tasks function
def view_pending_tasks():
    
    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks.")
        return
        
    for i, task in enumerate(pending_tasks):
        print(f"{i + 1}. Title: {task['title']}, Due Date: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress():
    
    total_tasks = len(tasks)
    if total_tasks == 0:
        return 0.0
    
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / total_tasks) * 100
    return progress