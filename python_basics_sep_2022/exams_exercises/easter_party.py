count_guests = int(input())
price_per_guest = float(input())
budget = float(input())

cake_price = budget * 0.1

if 10 <= count_guests <= 15:
    price_per_guest = price_per_guest * 0.85
elif 15 < count_guests <= 20:
    price_per_guest = price_per_guest * 0.8
elif count_guests > 20:
    price_per_guest = price_per_guest * 0.75
else:
    price_per_guest = price_per_guest

total_amount = cake_price + (count_guests * price_per_guest)
diff = abs(total_amount - budget)

if total_amount <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")
