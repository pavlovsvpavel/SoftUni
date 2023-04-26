n = int(input())

students_data = {}
for _ in range(n):
    student_name, grade = input().split(" ")
    if student_name not in students_data:
        students_data[student_name] = []

    students_data[student_name].append(float(grade))

for name, values in students_data.items():
    average_grade = sum(values) / len(values)
    all_grades_to_string = " ".join(map(lambda x: f'{x:.2f}', values))
    print(f"{name} -> {all_grades_to_string} (avg: {average_grade:.2f})")
