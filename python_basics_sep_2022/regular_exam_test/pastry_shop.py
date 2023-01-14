pastry_type = input()
count_pastry = int(input())
day = int(input())

price = 0
if pastry_type == "Cake" and day <= 15:
    price = count_pastry * 24
elif pastry_type == "Souffle" and day <= 15:
    price = count_pastry * 6.66
elif pastry_type == "Baklava" and day <= 15:
    price = count_pastry * 12.60

if pastry_type == "Cake" and day > 15:
    price = count_pastry * 28.70
elif pastry_type == "Souffle" and day > 15:
    price = count_pastry * 9.80
elif pastry_type == "Baklava" and day > 15:
    price = count_pastry * 16.98

if 100 <= price <= 200 and day <= 22:
    price = price * 0.85
elif price > 200 and day <= 22:
    price = price * 0.75
if day <= 15:
    price = price * 0.9

print(f"{price:.2f}")
