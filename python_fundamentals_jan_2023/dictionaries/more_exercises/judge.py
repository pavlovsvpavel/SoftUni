contests = {}
individual = {}
while True:
    data = input()

    if data == "no more time":
        break

    user_name, contest, points = [int(x) if x.isdigit() else x for x in data.split(" -> ")]

    contests[contest] = contests.get(contest, {})
    contests[contest][user_name] = contests[contest].get(user_name, 0)
    if contest in contests.keys():
        if contests[contest][user_name] < points:
            contests[contest][user_name] = points

for contest in contests.keys():
    print(f"{contest}: {len(contests[contest].values())} participants")
    for pos, (name, pts) in enumerate(sorted(contests[contest].items(), key=lambda i: (-i[1], i[0])), 1):
        print(f"{pos}. {name} <::> {pts}")
        individual[name] = individual.get(name, 0) + pts

print("Individual standings:")
for pos, (user, score) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f"{pos}. {user} -> {score}")
