"""
Develop a Python script that generates a right-angled triangle pattern.
The script should prompt the user to specify the number of rows. Here's a sample output for a user input of 5:
*
**
***
****
*****
"""

number_of_rows = int(input("Please enter the number of rows: "))

for i in range(number_of_rows):
    print("*" * (i + 1))