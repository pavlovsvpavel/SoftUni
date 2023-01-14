days = int(input())
type_of_room = input()
rating = input()

price = 0
nights = days - 1
if type_of_room == "room for one person":
    price = nights * 18
elif type_of_room == "apartment":
    if days < 10:
        price = nights * 25 * 0.70
    elif 10 <= days <= 15:
        price = nights * 25 * 0.65
    elif days > 15:
        price = nights * 25 * 0.5
elif type_of_room == "president apartment":
    if days < 10:
        price = nights * 35 * 0.90
    elif 10 <= days <= 15:
        price = nights * 35 * 0.85
    elif days > 15:
        price = nights * 35 * 0.80
if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.90
print(f"{price:.2f}")
