items_collection = input().split("|")
budget = float(input())

item_list = []
amount_of_sold_items = 0
new_prices_list = []
profit = 0
for item in items_collection:
    item_list = item.split("->")
    item_price = float(item_list[1])
    is_price_check = False

    if item_price <= budget:
        if "Clothes" in item_list and item_price <= 50:
            is_price_check = True
        elif "Shoes" in item_list and item_price <= 35:
            is_price_check = True
        elif "Accessories" in item_list and item_price <= 20.50:
            is_price_check = True
    else:
        continue

    if is_price_check:
        budget -= item_price
        new_price = item_price * 1.4
        profit += new_price - item_price
        amount_of_sold_items += new_price

        new_prices_list.append("{:.2f}".format(new_price))

total_amount = budget + amount_of_sold_items

print(*new_prices_list, sep=" ")
print(f"Profit: {profit:.2f}")

if total_amount >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")
