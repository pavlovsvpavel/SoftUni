from collections import deque
from math import floor


def multiply(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result *= nums[i]
    return result


def add(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result += nums[i]
    return result


def subtract(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result -= nums[i]
    return result


def divide(nums):
    result = nums[0]
    for i in range(1, len(nums)):
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
        if el == "*":
            numbers.append(multiply(numbers))
            numbers.rotate()
            numbers = removing_elements(numbers)
        elif el == "-":
            numbers.append(subtract(numbers))
            numbers.rotate()
            numbers = removing_elements(numbers)
        elif el == "+":
            numbers.append(add(numbers))
            numbers.rotate()
            numbers = removing_elements(numbers)
        elif el == "/":
            numbers.append(divide(numbers))
            numbers.rotate()
            numbers = removing_elements(numbers)

print(numbers[0])
