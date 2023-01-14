budget = float(input())
gender = input()
age = int(input())
type_of_sport = input()

price = 0

if type_of_sport == "Gym":
    if gender == "m":
        price = 42
    elif gender == "f":
        price = 35
elif type_of_sport == "Boxing":
    if gender == "m":
        price = 41
    elif gender == "f":
        price = 37
elif type_of_sport == "Yoga":
    if gender == "m":
        price = 45
    elif gender == "f":
        price = 42
elif type_of_sport == "Zumba":
    if gender == "m":
        price = 34
    elif gender == "f":
        price = 31
elif type_of_sport == "Dances":
    if gender == "m":
        price = 51
    elif gender == "f":
        price = 53
elif type_of_sport == "Pilates":
    if gender == "m":
        price = 39
    elif gender == "f":
        price = 37
if age <= 19:
    price = price * 0.80

diff = abs(price - budget)
if price <= budget:
    print(f"You purchased a 1 month pass for {type_of_sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")