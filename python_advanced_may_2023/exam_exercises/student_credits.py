def students_credits(*args):
    all_courses = {}
    credits_for_diploma = 240
    total_credits = 0
    courses_points = []
    for data in args:
        course_name, credit, max_points, student_points = [int(x) if x.isdigit() else x for x in data.split("-")]
        percentage_achieved = student_points / max_points
        course_credits = credit * percentage_achieved

        all_courses[course_name] = all_courses.get(course_name, course_credits)

    for curr_course, curr_credits in sorted(all_courses.items(), key=lambda x: -x[1]):
        total_credits += curr_credits
        courses_points.append(f"{curr_course} - {curr_credits:.1f}")

    if total_credits >= credits_for_diploma:
        return f"Diyan gets a diploma with {total_credits:.1f} credits." \
               f"\n{f'{chr(10)}'.join(courses_points)}"

    else:
        return f"Diyan needs {credits_for_diploma - total_credits:.1f} credits more for a diploma." \
               f"\n{f'{chr(10)}'.join(courses_points)}"


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
