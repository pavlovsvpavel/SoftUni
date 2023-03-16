import re

text = input()
total_calories = 0
items_list = []

pattern = r"(\#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>[\d]{2}\/[\d]{2}\/[\d]{2})\1" \
          r"(?P<calories>[\d]+)\1"

valid_input = re.finditer(pattern, text)

for el in valid_input:
    item = el["item"]
    date = el["date"]
    calories = int(el["calories"])
    total_calories += calories
    items_list.append(f"Item: {item}, Best before: {date}, Nutrition: {calories}")

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for item in items_list:
    print(item)
