products = {}
while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split(" ")

    if name not in products.keys():
        products[name] = [float(price), int(quantity)]
    else:
        products[name][0] = float(price)
        products[name][1] += int(quantity)

for name, price in products.items():
    total_price = price[0] * price[1]
    print(f"{name} -> {total_price:.2f}")

