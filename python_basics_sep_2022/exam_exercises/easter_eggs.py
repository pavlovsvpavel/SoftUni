eggs_count = int(input())

red_count = 0
orange_count = 0
blue_count = 0
green_count = 0

for i in range(1, eggs_count + 1):
    if i > eggs_count:
        break

    egg_color = input()

    if egg_color == "red":
        red_count += 1
    elif egg_color == "orange":
        orange_count += 1
    elif egg_color == "blue":
        blue_count += 1
    elif egg_color == "green":
        green_count += 1

color = {"red": red_count, "blue": blue_count, "orange": orange_count, "green": green_count}
print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max(red_count, orange_count, blue_count, green_count)} -> {max(color, key=color.get)}")




