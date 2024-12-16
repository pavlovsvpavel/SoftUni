"""
Write a Python script that displays a diamond pattern
based on the number of rows (height) specified by the user.
For instance, if the user enters 5, the output should resemble the following:
  *
 ***
*****
 ***
  *
"""

while True:
    size_of_diamond = int(input("Enter the size of the diamond pattern: "))

    if size_of_diamond % 2 == 0:
        print("Please enter odd number for size of diamond.")
        continue

    middle = size_of_diamond // 2

    for i in range(middle + 1):
        for j in range(middle - i):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(middle - 1, -1, -1):
        for j in range(middle - i):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    break
