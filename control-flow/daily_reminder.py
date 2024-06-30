task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound.lower() == "yes":
    immediate_attention = "that requires immediate attention today!"
else:
    immediate_attention = "Consider completing it when you have free time."

print(f"Reminder: '{task}' is a {priority} priority task {immediate_attention}")