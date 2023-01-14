from math import floor
from math import ceil
days_count = int(input())
food_kg = int(input())
dog_food_kg_per_day = float(input())
cat_food_kg_per_day = float(input())
turtle_food_g_per_day = float(input())

dog_food_needed = dog_food_kg_per_day * days_count
cat_food_needed = cat_food_kg_per_day * days_count
turtle_food_needed = turtle_food_g_per_day / 1000 * days_count

total_kg_needed = (dog_food_needed + cat_food_needed + turtle_food_needed)
diff = abs(food_kg - total_kg_needed)

if food_kg >= total_kg_needed:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
