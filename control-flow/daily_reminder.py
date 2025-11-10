# daily_reminder.py
# Author: Mahamat Youssouf Djibrine
# Objective: Remind the user about a priority task using conditionals, match-case, and loops.

# Run loop to ensure valid input
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task description cannot be empty. Please enter again.")

# Ask for task priority
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ("high", "medium", "low"):
        break
    print("Invalid input! Please enter high, medium, or low.")

# Ask if task is time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ("yes", "no"):
        break
    print("Please answer 'yes' or 'no'.")

# Generate reminder using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task with unspecified priority"

# Add conditional message for time-sensitive tasks
if time_bound == "yes":
    reminder += " that requires immediate attention today! ⚡"
else:
    reminder += ". Consider completing it when you have free time. 🕒"

# Display final reminder
print("\nReminder:", reminder)
print("\n✅ Great job using Python conditionals and match-case!")
