def gather_credits(needed_credits, *courses):
    total_credits = 0
    enrolled_courses = []

    def print_func(flag=True):
        if flag:
            return f"Enrollment finished! Maximum credits: {total_credits}.\n" \
                   f"Courses: {', '.join(sorted(enrolled_courses, reverse=False))}"
        else:
            return f"You need to enroll in more courses! " \
                   f"You have to gather {needed_credits - total_credits} credits more."

    if total_credits == needed_credits:
        return print_func()

    for course in courses:

        if course[0] in enrolled_courses:
            continue

        if total_credits < needed_credits:
            total_credits += course[1]
            enrolled_courses.append(course[0])

        if total_credits >= needed_credits:
            return print_func()

    return print_func(False)


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    0,
    ("Basics-20", 27),
    ("Basic-5", 12),
    ("Basics-3", 50),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

