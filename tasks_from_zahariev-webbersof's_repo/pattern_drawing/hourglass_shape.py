"""
Design a Python program to display an hourglass shape.
The user should specify the number of rows.
If the user inputs 4, the output should be:
*******
 *****
  ***
   *
  ***
 *****
*******
"""

number_of_rows = int(input("Enter the number of rows: "))

for i in range(number_of_rows, 0, -1):
    for j in range(number_of_rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(2, number_of_rows + 1):
    for j in range(number_of_rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()