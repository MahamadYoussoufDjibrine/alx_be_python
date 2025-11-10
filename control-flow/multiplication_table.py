# multiplication_table.py
# Author: Mahamat Youssouf Djibrine
# Objective: Generate a multiplication table for a user-defined number

# Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate the multiplication table using a for loop
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# Output
# Enter a number to see its multiplication table: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50