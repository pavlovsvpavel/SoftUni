from collections import deque

bowls = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while bowls and customers:
    current_bow = bowls.pop()
    current_customer = customers.popleft()

    if current_bow == current_customer:
        continue

    elif current_bow > current_customer:
        current_bow -= current_customer
        bowls.append(current_bow)

    elif current_customer > current_bow:
        current_customer -= current_bow
        customers.appendleft(current_customer)

if customers:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")

if bowls:
    print(f"Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")

if not customers and not bowls:
    print(f"Great job! You served all the customers.")

