items = input().split(" ")
stock = {}
searched_products = input().split(" ")

for index in range(0, len(items), 2):
    products = items[index]
    quantities = items[index + 1]
    stock[products] = int(quantities)

for product in searched_products:
    if product in stock:
        quantity = stock[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
