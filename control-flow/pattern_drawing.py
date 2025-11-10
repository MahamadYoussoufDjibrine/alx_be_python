# pattern_drawing.py
# Author: Mahamat Youssouf Djibrine
# Objective: Draw a square pattern using nested loops

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns (printing asterisks)
    for col in range(size):
        print("*", end="")  # Print on same line
    print()  # Move to next line after each row
    row += 1  # Increment row counter
