food_kg = int(input()) * 1000

food_per_eat_g = input()
total_food_g = 0
flag = False

while food_per_eat_g != "Adopted":
    food_per_eat_g = int(food_per_eat_g)
    total_food_g += food_per_eat_g

    food_per_eat_g = input()

diff = abs(total_food_g - food_kg)

if total_food_g > food_kg:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")

