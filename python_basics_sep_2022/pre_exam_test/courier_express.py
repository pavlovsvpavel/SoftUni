package_weight = float(input())
type_of_delivery = input()
distance_km = int(input())

price = 0

if package_weight < 1:
    price = distance_km * 0.03
elif 1 <= package_weight < 10:
    price = distance_km * 0.05
elif 10 <= package_weight < 40:
    price = distance_km * 0.10
elif 40 <= package_weight < 90:
    price = distance_km * 0.15
elif 90 <= package_weight < 150:
    price = distance_km * 0.20

if type_of_delivery == "express":
    if package_weight < 1:
        price_kg = package_weight * (0.03 * 0.8)
        price += distance_km * price_kg
    elif 1 <= package_weight < 10:
        price_kg = package_weight * (0.05 * 0.4)
        price += distance_km * price_kg
    elif 10 <= package_weight < 40:
        price_kg = package_weight * (0.10 * 0.05)
        price += distance_km * price_kg
    elif 40 <= package_weight < 90:
        price_kg = package_weight * (0.15 * 0.02)
        price += distance_km * price_kg
    elif 90 <= package_weight < 150:
        price_kg = package_weight * (0.20 * 0.01)
        price += distance_km * price_kg

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {price:.2f} lv.")

