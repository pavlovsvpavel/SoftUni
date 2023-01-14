name = input()

counter = 0
sum_grades = 0
poor_grades = 0
while True:
    grade = float(input())
    counter += 1

    if grade < 4.00:
        poor_grades += 1
        if poor_grades == 2:
            print(f"{name} has been excluded at {counter} grade")
            break

        counter -= 1

    if grade >= 4.00:
        sum_grades += grade

    if counter == 12:
        average_grade = sum_grades / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
