# daily_reminder.py
# Author: Mahamat Youssouf Djibrine
# Objective: Display a personalized daily reminder based on time of day

# Function to display greeting based on time
def daily_reminder(hour):
    if 5 <= hour < 12:
        print("🌅 Good morning! Time to start your day strong 💪.")
        print("Don’t forget to exercise and have a healthy breakfast!")
    elif 12 <= hour < 18:
        print("🌞 Good afternoon! Stay productive and focused.")
        print("Take a short break and hydrate 💧.")
    elif 18 <= hour < 22:
        print("🌆 Good evening! You did great today.")
        print("Spend time relaxing or with family ❤️.")
    else:
        print("🌙 It’s late! Time to rest and recharge 💤.")

# Ask user for the current hour
try:
    current_hour = int(input("Enter the current hour (0–23): "))
    if 0 <= current_hour <= 23:
        daily_reminder(current_hour)
    else:
        print("Please enter a valid hour between 0 and 23.")
except ValueError:
    print("Invalid input! Please enter a number between 0 and 23.")
