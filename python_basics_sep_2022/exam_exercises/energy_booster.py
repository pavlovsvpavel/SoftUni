flavour = input()
set_size = input()
set_count = int(input())
price = 0

if set_size == "small":
    if flavour == "Watermelon":
        price = set_count * 2 * 56
    elif flavour == "Mango":
        price = set_count * 2 * 36.66
    elif flavour == "Pineapple":
        price = set_count * 2 * 42.10
    elif flavour == "Raspberry":
        price = set_count * 2 * 20
elif set_size == "big":
    if flavour == "Watermelon":
        price = set_count * 5 * 28.70
    elif flavour == "Mango":
        price = set_count * 5 * 19.60
    elif flavour == "Pineapple":
        price = set_count * 5 * 24.80
    elif flavour == "Raspberry":
        price = set_count * 5 * 15.20

if 400 <= price <= 1000:
    price = price * 0.85
elif price > 1000:
    price = price * 0.5

print(f"{price:.2f} lv.")
