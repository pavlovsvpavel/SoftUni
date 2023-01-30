def total_price(product, qty):
    if product == "coffee":
        return qty * 1.50
    elif product == "water":
        return qty * 1.00
    elif product == "coke":
        return qty * 1.40
    elif product == "snacks":
        return qty * 2.00


user_product = input()
current_quantity = int(input())

print(f"{total_price(user_product, current_quantity):.2f}")
