import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student


def add_students():
    # STUDENTS = [
    #     {
    #         'student_id': 'FC5204',
    #         'first_name': 'John',
    #         'last_name': 'Doe',
    #         'birth_date': '1995-05-15',
    #         'email': 'john.doe@university.com'
    #     },
    #     {
    #         'student_id': 'FE0054',
    #         'first_name': 'Jane',
    #         'last_name': 'Smith',
    #         'email': 'jane.smith@university.com'
    #     },
    #     {
    #         'student_id': 'FH2014',
    #         'first_name': 'Alice',
    #         'last_name': 'Johnson',
    #         'birth_date': '1998-02-10',
    #         'email': 'alice.johnson@university.com'
    #     },
    #     {
    #         'student_id': 'FH2015',
    #         'first_name': 'Bob',
    #         'last_name': 'Wilson',
    #         'birth_date': '1996-11-25',
    #         'email': 'bob.wilson@university.com'
    #     }
    # ]
    #
    # for student in STUDENTS:
    #     Student.objects.create(**student)

    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )

    Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )


def get_students_info():
    all_students = []

    for student in Student.objects.all():
        all_students.append(
            f"Student №{student.student_id}: "
            f"{student.first_name} {student.last_name}; "
            f"Email: {student.email}"
        )

    return "\n".join(all_students)


def update_students_emails():
    for c_student in Student.objects.all():
        new_email = c_student.email.replace('university.com', 'uni-students.com')
        c_student.email = new_email
        c_student.save()


def truncate_students():
    Student.objects.all().delete()


# add_students()
# print(Student.objects.all())
# print(get_students_info())
# update_students_emails()
# for student in Student.objects.all():
#     print(student.email)
# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")
