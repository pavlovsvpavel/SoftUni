count_students = int(input())

sum_of_grades = 0
count_top = 0
count_between_4_5 = 0
count_between_3_4 = 0
count_fail = 0

for i in range(1, count_students + 1):
    grade = float(input())
    sum_of_grades += grade
    if 2 <= grade <= 2.99:
        count_fail += 1
    elif 3 <= grade <= 3.99:
        count_between_3_4 += 1
    elif 4 <= grade <= 4.99:
        count_between_4_5 += 1
    elif grade >= 5:
        count_top += 1

average_grade = sum_of_grades / count_students
percent_top = count_top / count_students * 100
percent_between_4_5 = count_between_4_5 / count_students * 100
percent_between_3_4 = count_between_3_4 / count_students * 100
percent_fail = count_fail / count_students * 100

print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_3_4:.2f}%")
print(f"Fail: {percent_fail:.2f}%")
print(f"Average: {average_grade:.2f}")


