"""
Write a Python script that prints a square pattern where stars and dashes alternate in each row.
The size of the square should be provided by the user. Here's an example for user input of 5:
*-*-*
-*-*-
*-*-*
-*-*-
*-*-*
"""

number_of_rows = int(input("Enter the number of rows: "))

for i in range(number_of_rows):
    for j in range(number_of_rows):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print("-", end="")
    print()