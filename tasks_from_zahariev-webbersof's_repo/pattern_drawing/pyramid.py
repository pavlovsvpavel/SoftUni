"""
Create a Python script that prints a pyramid pattern based on the user-input number of rows.
For example, if the user inputs 4, the output should be:
   *
  ***
 *****
*******
"""
height_of_pyramid = int(input("Enter the height of pyramid pattern: "))

for i in range(height_of_pyramid):
    for j in range(height_of_pyramid - 1 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()