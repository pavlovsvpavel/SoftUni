import sys
easter_bread_count = int(input())

max_points = - sys.maxsize
best_chef = ""

for i in range(1, easter_bread_count + 1):
    chef_name = input()
    total_points = 0
    while True:
        points = input()

        if points == "Stop":
            print(f"{chef_name} has {total_points} points.")
            break
        else:
            points = int(points)

        total_points += points

    if total_points > max_points:
        max_points = total_points
        best_chef = chef_name
        print(f"{best_chef} is the new number 1!")

print(f"{best_chef} won competition with {max_points} points!")
