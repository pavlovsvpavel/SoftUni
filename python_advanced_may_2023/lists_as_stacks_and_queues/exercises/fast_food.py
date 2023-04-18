from collections import deque

food_qty = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))
while orders:
    order = orders.popleft()
    if food_qty - order >= 0:
        food_qty -= order
    else:
        print(f"Orders left: {order}", *orders)
        break
else:
    print("Orders complete")
