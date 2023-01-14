budget = float(input())
season = input()

car_class = ""
type_of_car = ""
price_for_car = 0
if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        price_for_car = budget * 0.35
        type_of_car = "Cabrio"
    else:
        price_for_car = budget * 0.65
        type_of_car = "Jeep"

if 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        price_for_car = budget * 0.45
        type_of_car = "Cabrio"
    else:
        price_for_car = budget * 0.80
        type_of_car = "Jeep"

if budget > 500:
    car_class = "Luxury class"
    price_for_car = budget * 0.90
    type_of_car = "Jeep"

print(car_class)
print(f"{type_of_car} - {price_for_car:.2f}")
