count_students = int(input())

top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
below_3 = 0
sum_grades = 0
for _ in range(1, count_students + 1):
    grade = float(input())
    if grade >= 5:
        top_students += 1
        sum_grades += grade
    elif 4.00 <= grade <= 4.99:
        between_4_and_5 += 1
        sum_grades += grade
    elif 3.00 <= grade <= 3.99:
        between_3_and_4 += 1
        sum_grades += grade
    else:
        below_3 += 1
        sum_grades += grade

average_grade = sum_grades / count_students
print(f"Top students: {top_students / count_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5 / count_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4 / count_students * 100:.2f}%")
print(f"Fail: {below_3 / count_students * 100:.2f}%")
print(f"Average: {average_grade:.2f}")




