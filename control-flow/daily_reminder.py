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
    beginning_message = "Reminder"
    ending_message = " that requires immediate attention today!"
else:
    beginning_message = "Note"
    ending_message = ". Consider completing it when you have free time."

print()
print(f"{beginning_message}: '{task}' is a {level} priority task{ending_message}")