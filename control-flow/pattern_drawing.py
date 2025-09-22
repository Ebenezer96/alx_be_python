# pattern_drawing.py
# A program to draw a square pattern of asterisks using while and nested for loops.

# Prompt user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to control rows
while row < size:
    # Use a for loop to print asterisks for each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing one row
    print()
    # Increment row counter
    row += 1
