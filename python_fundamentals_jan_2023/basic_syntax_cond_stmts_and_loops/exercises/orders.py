count_orders = int(input())

order_amount = 0
total_amount = 0

for _ in range(count_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if price_per_capsule > 100 or price_per_capsule < 0.01 or days > 31 or days < 1 or capsules_per_day > 2000 \
            or capsules_per_day < 1:
        continue

    else:
        order_amount = capsules_per_day * price_per_capsule * days
        print(f"The price for the coffee is: ${order_amount:.2f}")

    total_amount += order_amount

print(f"Total: ${total_amount:.2f}")
