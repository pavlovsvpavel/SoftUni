days = int(input())
food_in_g = float(input())

eaten_food = 0
biscuits = 0
dog_food_total = 0
cat_food_total = 0

for i in range(1, days + 1):
    dog_food = float(input())
    cat_food = float(input())
    eaten_food += dog_food + cat_food
    dog_food_total += dog_food
    cat_food_total += cat_food
    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.1

percent_eaten_food = eaten_food / food_in_g * 100
percent_dog_food = dog_food_total / eaten_food * 100
percent_cat_food = cat_food_total / eaten_food * 100

print(f"Total eaten biscuits: {biscuits:.0f}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")



