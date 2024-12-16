"""
Craft a Python script to print a mirrored right-angled triangle pattern.
The user provides the number of rows.
For example, if the user inputs 5, the output should resemble:
    *
   **
  ***
 ****
*****
"""

number_of_rows = int(input("Enter the size of the diamond pattern: "))

for i in range(1, number_of_rows + 1):
    for j in range(number_of_rows - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")

    print()