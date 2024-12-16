"""
Craft a Python program that produces a square pattern with a hollow center.
The program should take the size of the square as input from the user.
Here's an example output for a user input of 5:
*****
*   *
*   *
*   *
*****
"""

size_of_the_square = int(input("Enter the size of the square: "))

for i in range(size_of_the_square):
    for j in range(size_of_the_square):
        if i == 0 or i == size_of_the_square - 1 or j == 0 or j == size_of_the_square - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()