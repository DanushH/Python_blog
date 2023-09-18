# Define a list of days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Define a tuple representing task categories
task_categories = ("Work", "Home", "Errands")

# Initialize an empty dictionary to store tasks for each day
task_manager = {day: [] for day in days_of_week}

# Initialize an empty set to store unique task names
unique_tasks = set()

# Function to add a task for a specific day
def add_task(day, task_name, category):
    if day in task_manager:
        task = {"name": task_name, "category": category}
        if task_name not in unique_tasks:
            task_manager[day].append(task)
            unique_tasks.add(task_name)
            print(f"Task '{task_name}' added to {day}'s tasks.")
        else:
            print(f"Task '{task_name}' already exists in the task list.")
    else:
        print("Invalid day of the week.")

# Function to display tasks for a specific day
def display_tasks(day):
    if day in task_manager:
        tasks = task_manager[day]
        if tasks:
            print(f"Tasks for {day}:")
            for task in tasks:
                print(f"- {task['name']} ({task['category']})")
        else:
            print(f"No tasks for {day}.")
    else:
        print("Invalid day of the week.")

# Add some tasks to the task manager
add_task("Monday", "Finish project report", "Work")
add_task("Monday", "Grocery shopping", "Errands")
add_task("Tuesday", "Clean the house", "Home")
add_task("Wednesday", "Meeting with client", "Work")

# Display tasks for specific days
display_tasks("Monday")
display_tasks("Tuesday")
display_tasks("Wednesday")
display_tasks("Saturday")  # Invalid day

# Print the task categories
print("Task categories:", task_categories)
