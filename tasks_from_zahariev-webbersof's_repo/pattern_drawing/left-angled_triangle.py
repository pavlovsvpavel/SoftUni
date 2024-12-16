"""
Design a Python code snippet to print a left-angled triangle pattern.
The user should provide the number of rows. For instance, if the user inputs 4, the output should be:
****
***
**
*
"""

number_of_rows = int(input("Please enter the number of rows: "))

for i in range(number_of_rows -1, -1, -1):
    print("*" * (i + 1))