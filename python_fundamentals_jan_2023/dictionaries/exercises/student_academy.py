students = {}
count_students = int(input())

for _ in range(count_students):
    name = input()

    if name not in students.keys():
        students[name] = []

    students[name].append(float(input()))

for student in list(students.keys()):
    avg_grade = sum(students[student]) / len(students[student])
    if avg_grade < 4.50:
        del students[student]
    else:
        print(f"{student} -> {avg_grade:.2f}")
