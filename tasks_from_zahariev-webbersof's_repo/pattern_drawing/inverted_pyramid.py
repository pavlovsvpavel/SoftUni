"""
Develop a Python script that prints an inverted pyramid pattern based on the number of rows provided by the user.
For instance, if the user inputs 5, the output should be:
*********
 *******
  *****
   ***
    *
"""

height_of_pyramid = int(input("Enter the height of pyramid pattern: "))

for i in range(height_of_pyramid - 1, -1, -1):
    for j in range(height_of_pyramid - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()