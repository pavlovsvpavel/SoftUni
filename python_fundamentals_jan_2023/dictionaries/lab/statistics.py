products = {}
while True:
    command = input()

    if command == "statistics":
        break

    items = command.split(": ")
    product = items[0]
    quantity = int(items[1])

    # if product not in products:
    #     products[product] = 0
    # products[product] += int(quantity)

    products[product] = products.get(product, 0) + quantity

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

