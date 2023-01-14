fats_percent = int(input())
proteins_percent = int(input())
carbohydrates_percent = int(input())
calories = int(input())
water_percent = int(input())

fats = calories * (fats_percent / 100) / 9
proteins = calories * (proteins_percent / 100) / 4
carbohydrates = calories * (carbohydrates_percent / 100) / 4

food_in_g = fats + proteins + carbohydrates
calories_per_g = calories / food_in_g

calories_without_water = calories_per_g * (100 - water_percent) / 100

print(f"{calories_without_water:.4f}")
