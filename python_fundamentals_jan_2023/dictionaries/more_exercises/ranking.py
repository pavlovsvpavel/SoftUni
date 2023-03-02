contests_passwords = {}
students = {}
while True:
    contests_data = input()

    if contests_data == "end of contests":
        break

    contest_name, contest_password = contests_data.split(":")
    contests_passwords[contest_name] = contests_passwords.get(contest_name, contest_password)

while True:
    users_data = input()
    if users_data == "end of submissions":
        break

    contest, password, user, points = users_data.split("=>")
    points = int(points)

    if contest in contests_passwords.keys() and password == contests_passwords[contest]:
        students[user] = students.get(user, {})
        students[user][contest] = students[user].get(contest, 0)
        if points > students[user][contest]:
            students[user][contest] = points

candidates = {user: sum(students[user].values()) for user in students}
best_candidate = max(candidates, key=lambda i: candidates[i])

print(f"Best candidate is {best_candidate} with total {candidates[best_candidate]} points.")
print("Ranking:")
for user in sorted(students):
    print(f"{user}")
    for course, points in sorted(students[user].items(), key=lambda x: -x[1]):
        print(f"#  {course} -> {points}")
