poor_grades = int(input())
task_name = input()

sum_grades = 0
count_tasks = 0
count_poor_grades = 0
last_task = ""
average_grade = 0
flag = False
while task_name != "Enough":
    grade = int(input())
    sum_grades += grade
    count_tasks += 1

    if grade <= 4:
        count_poor_grades += 1
        if count_poor_grades == poor_grades:
            flag = True
            break

    last_task = task_name
    task_name = input()

    if task_name == "Enough":
        break

if flag:
    print(f"You need a break, {count_poor_grades} poor grades.")
else:
    average_grade = sum_grades / count_tasks
    print(f"Average score: {average_grade:.2f}\nNumber of problems: {count_tasks}\nLast problem: {last_task}")




