courses = {}
while True:
    command = input()

    if command == "end":
        break

    course_name, student_name = command.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = []

    courses[course_name].append(student_name)

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for name in courses[course_name]:
        print(f"-- {name}")

