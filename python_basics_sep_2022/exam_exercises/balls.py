from math import floor
count_balls = int(input())

points = 0
count_red = 0
count_orange = 0
count_yellow = 0
count_white = 0
count_black = 0

for i in range(1, count_balls + 1):
    color = input()
    if color == "red":
        points += 5
        count_red += 1
    elif color == "orange":
        points += 10
        count_orange += 1
    elif color == "yellow":
        points += 15
        count_yellow += 1
    elif color == "white":
        points += 20
        count_white += 1
    elif color == "black":
        points = floor(points / 2)
        count_black += 1
    else:
        points = points

count_others = count_balls - (count_red + count_orange + count_yellow + count_white + count_black)

print(f"Total points: {points}")
print(f"Red balls: {count_red}")
print(f"Orange balls: {count_orange}")
print(f"Yellow balls: {count_yellow}")
print(f"White balls: {count_white}")
print(f"Other colors picked: {count_others}")
print(f"Divides from black balls: {count_black}")

