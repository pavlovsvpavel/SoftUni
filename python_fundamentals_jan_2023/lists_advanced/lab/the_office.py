employees_happiness = input().split(" ")
factor = int(input())

current_happiness = list(map(lambda x: int(x) * factor, employees_happiness))
avg_happiness = sum(current_happiness) / len(current_happiness)
filtered_employees = list(filter(lambda x: x >= avg_happiness, current_happiness))

if len(filtered_employees) >= len(employees_happiness) / 2:
    print(f"Score: {len(filtered_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees)}/{len(employees_happiness)}. Employees are not happy!")
