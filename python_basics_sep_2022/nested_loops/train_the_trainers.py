count_jury = int(input())
presentation_name = input()

sum_of_grades_total = 0
total_grades = 0
while presentation_name != "Finish":
    average_grade_for_presentation = 0
    sum_of_grades_per_presentation = 0
    for i in range(1, count_jury + 1):
        grade = float(input())
        total_grades += 1
        sum_of_grades_per_presentation += grade
    average_grade_for_presentation = sum_of_grades_per_presentation / count_jury
    sum_of_grades_total += sum_of_grades_per_presentation
    print(f"{presentation_name} - {average_grade_for_presentation:.2f}.")

    presentation_name = input()

average_all_presentations = sum_of_grades_total / total_grades

print(f"Student's final assessment is {average_all_presentations:.2f}.")




