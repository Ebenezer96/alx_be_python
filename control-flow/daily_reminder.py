# daily_reminder.py
# A program that reminds the user of a single priority task using match case, conditionals, and loops.

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Loop to ensure the reminder is displayed at least once
reminder_shown = False

while not reminder_shown:
    # Match Case for priority handling
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unspecified priority level"

    # Add time-sensitivity condition
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder = "Note: " + reminder + ". Consider completing it when you have free time."

    # Final reminder message
    print("\nReminder:", reminder)

    # Exit loop after first reminder (keeps logic simple per requirements)
    reminder_shown = True
