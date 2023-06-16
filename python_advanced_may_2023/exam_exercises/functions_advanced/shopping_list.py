def shopping_list(budget, **kwargs):
    products = {}
    result = []
    if budget < 100:
        return "You do not have enough budget."

    for item, info in kwargs.items():
        if len(products) == 5:
            break

        amount = float(info[0]) * info[1]

        if amount <= budget:
            products[item] = amount
            budget -= amount

    for product, total_amount in products.items():
        result.append(f"You bought {product} for {total_amount:.2f} leva.")

    return "\n".join(result)


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))


print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

#
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
