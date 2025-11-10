# weather_advice.py
# Author: Mahamat Youssouf Djibrine
# Objective: Give clothing recommendations based on weather conditions

# Ask the user for the weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
