import math

days = int(input())
food_kg = int(input())
first_deer_food_per_day = float(input())
second_deer_food_per_day = float(input())
third_deer_food_per_day = float(input())

first_deer_food_total = first_deer_food_per_day * days
second_deer_food_per_total = second_deer_food_per_day * days
third_deer_food_per_total = third_deer_food_per_day * days

needed_food = first_deer_food_total + second_deer_food_per_total + third_deer_food_per_total

diff = abs(needed_food - food_kg)

if needed_food <= food_kg:
    diff = math.floor(diff)
    print(f"{diff} kilos of food left.")
else:
    diff = math.ceil(diff)
    print(f"{diff} more kilos of food are needed.")
