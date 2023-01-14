month = input()
nights_count = int(input())

price_studio = 0
price_apartment = 0

if month in ["May", "October"]:
    price_studio = nights_count * 50
    price_apartment = nights_count * 65
    if month in ["May", "October"] and 7 < nights_count <= 14:
        price_studio = price_studio * 0.95
        price_apartment = price_apartment
    elif month in ["May", "October"] and nights_count > 14:
        price_studio = price_studio * 0.70
        price_apartment = price_apartment * 0.90

if month in ["June", "September"]:
    price_studio = nights_count * 75.20
    price_apartment = nights_count * 68.70
    if month in ["June", "September"] and nights_count > 14:
        price_studio = price_studio * 0.80
        price_apartment = price_apartment * 0.90

if month in ["July", "August"]:
    price_studio = nights_count * 76
    price_apartment = nights_count * 77
    if month in ["July", "August"] and nights_count > 14:
        price_studio = nights_count * 76
        price_apartment = price_apartment * 0.90

print(f"Apartment: {price_apartment:.2f} lv.\nStudio: {price_studio:.2f} lv.")
