task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "low":
        level = "low"
    case "medium":
        level = "medium"
    case "high":
        level = "high"
if time_bound == "yes":
    print()
    print(f"Reminder: '{task}' is a {level} priority task that requires immediate attention today!")
else:
    print()
    print(f"Note: '{task}' is a {level} priority task. Consider completing it when you have free time.")