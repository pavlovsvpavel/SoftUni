open_tabs = int(input())
init_salary = int(input())
penalty = 0
total_penalty = 0
for i in range(1, open_tabs + 1):
    tab_name = input()
    if tab_name == "Facebook":
        penalty = 150
        total_penalty += penalty
    elif tab_name == "Instagram":
        penalty = 100
        total_penalty += penalty
    elif tab_name == "Reddit":
        penalty = 50
        total_penalty += penalty
    if total_penalty >= init_salary:
        break

if total_penalty == init_salary:
    print("You have lost your salary.")
else:
    diff = init_salary - total_penalty
    print(diff)
