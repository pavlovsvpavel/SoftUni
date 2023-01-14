points = int(input())
total_points = 0
bonus_points = 0

if points <= 100:
    bonus_points = 5
    total_points = points + bonus_points
elif 100 < points < 1000:
    bonus_points = points * 0.20
    total_points = points + bonus_points
elif points > 1000:
    bonus_points = points * 0.1
    total_points = points + bonus_points

if points % 2 == 0:
    bonus_points = bonus_points + 1
    total_points = bonus_points + points
elif points % 10 == 5:
    bonus_points = bonus_points + 2
    total_points = bonus_points + points

print(f"{bonus_points}\n{total_points}")

