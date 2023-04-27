from collections import deque
from math import floor


def calculations(nums, operator):
    result = nums[0]
    for i in range(1, len(nums)):
        if operator == "*":
            result *= nums[i]
        elif operator == "+":
            result += nums[i]
        elif operator == "-":
            result -= nums[i]
        elif operator == "/":
            result /= nums[i]
    return floor(result)


def removing_elements(lst):
    for idx in range(1, len(lst)):
        lst.pop()
    return lst


expression = input().split(" ")

numbers = deque()
operators = ["*", "+", "-", "/"]
for el in expression:
    if el not in operators:
        numbers.append(int(el))
    else:
        numbers.append(calculations(numbers, el))
        numbers.rotate()
        numbers = removing_elements(numbers)

print(numbers[0])