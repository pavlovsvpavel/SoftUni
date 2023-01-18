import math

total_persons = int(input())
capacity_per_course = int(input())

courses = math.ceil(total_persons / capacity_per_course)

print(courses)
