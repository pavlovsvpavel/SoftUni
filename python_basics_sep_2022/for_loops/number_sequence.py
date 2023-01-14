import sys
max_number = -sys.maxsize
min_number = sys.maxsize
number_of_lines = int(input())

for _ in range(number_of_lines):
    num = int(input())
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print(f"Max number: {max_number}\nMin number: {min_number}")

