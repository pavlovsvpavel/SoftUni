company_users = {}

while True:
    command = input()

    if command == "End":
        break

    company, employee_id = command.split(" -> ")

    if company not in company_users.keys():
        company_users[company] = []
    elif employee_id in company_users[company]:
        continue

    company_users[company].append(employee_id)

for company in company_users.keys():
    print(f"{company}")
    for employee_id in company_users[company]:
        print(f"-- {employee_id}")
