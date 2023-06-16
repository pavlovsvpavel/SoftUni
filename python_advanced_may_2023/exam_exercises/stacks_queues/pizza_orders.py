from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = deque(int(x) for x in input().split(", "))

total_pizzas = 0

while orders and employees:
    order = orders.popleft()
    employee = employees.pop()

    if order > 10:
        employees.append(employee)
        continue

    if order <= 0:
        employees.append(employee)
        continue

    if order <= employee:
        total_pizzas += order

    elif order > employee:
        total_pizzas += employee
        orders.appendleft(order - employee)

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(map(str, employees))}")

if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, orders))}")
