from datetime import datetime

def validate_task_title(title):
    if not title.strip():
        print("Error: Task title cannot be empty.")
        return False
    return True
    None
    
def validate_task_description(description):
    
    if len(description.strip()) < 5:
        print("Error: Task description must be at least 5 characters long.")
        return False
    return True

    None    
    
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Due date must be in YEAR-MONTH-DAY format.")
        return False
    None
