def shop_from_grocery_list(*args):
    budget = 0
    grocery_list = []
    products = []

    for element in args:
        if type(element) is int:
            budget = element

        elif type(element) == list:
            grocery_list.extend(element)

        elif type(element) == tuple:
            products.append(element)

    for product, price in products:
        if product in grocery_list:
            if price <= float(budget):
                budget -= price
                grocery_list.remove(product)
            else:
                break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))

# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))
