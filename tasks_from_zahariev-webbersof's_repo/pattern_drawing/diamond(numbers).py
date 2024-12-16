"""
Write a Python program that prints a diamond shape pattern with numbers.
The user provides the number of rows for the top half of the diamond.
If the user inputs 4, the output should look like this:
   1
  121
 12321
1234321
 12321
  121
   1
"""

size_of_diamond = int(input("Enter the size of the diamond pattern: "))

for i in range(1, size_of_diamond + 1):
    for j in range(size_of_diamond - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print()

for i in range(size_of_diamond -1, 0, -1):
    for j in range(size_of_diamond - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    for l in range(i - 1, 0, -1):
        print(l, end="")
    print()