def shopping_cart(*args):
    cart_dict = {
        "Pizza": [],
        "Soup": [],
        "Dessert": [],
    }

    result = []

    for data in args:
        if data == "Stop":
            break

        meal, product = data

        if meal == "Pizza" and len(cart_dict["Pizza"]) == 4:
            continue

        if meal == "Soup" and len(cart_dict["Soup"]) == 3:
            continue

        if meal == "Dessert" and len(cart_dict["Dessert"]) == 2:
            continue

        if product not in cart_dict[meal]:
            cart_dict[meal].append(product)

    for product in cart_dict.values():
        if len(product) > 0:
            break
    else:
        return "No products in the cart!"

    for meal_name, product_names in sorted(
            cart_dict.items(), key=lambda x: (-len(x[1]), x[0])):

        result.append(f"{meal_name}:")

        for product_name in sorted(product_names, reverse=False):
            if product_names:
                result.append(f" - {product_name}")

    return "\n".join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
