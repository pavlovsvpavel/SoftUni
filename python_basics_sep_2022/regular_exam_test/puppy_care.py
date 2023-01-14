food_g = int(input()) * 1000

eaten_food_g = input()
total_eaten_food_g = 0

while True:
    if eaten_food_g != "Adopted":
        eaten_food_g = int(eaten_food_g)
        total_eaten_food_g += eaten_food_g
    else:
        break

    eaten_food_g = input()


diff = abs(food_g - total_eaten_food_g)

if food_g >= total_eaten_food_g:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")





