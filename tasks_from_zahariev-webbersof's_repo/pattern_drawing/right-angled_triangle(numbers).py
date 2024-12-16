"""
Write a Python program that prints a right-angled triangle using numbers.
The user will provide the number of rows. For example, if the user inputs 5, the output should look like this:
1
12
123
1234
12345
"""

number_of_rows = int(input("Please enter the number of rows: "))

for i in range(1, number_of_rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()