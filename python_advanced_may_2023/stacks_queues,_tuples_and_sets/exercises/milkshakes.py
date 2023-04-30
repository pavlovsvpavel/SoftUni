from collections import deque


def print_func(lst):
    if lst:
        return ", ".join(map(str, lst))


chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0
while len(chocolates) > 0 and len(cups_of_milk) > 0:
    if milkshakes == 5:
        break
    last_chocolate = chocolates[len(chocolates) - 1]
    first_cup = cups_of_milk[0]
    if last_chocolate <= 0 or first_cup <= 0:
        if last_chocolate <= 0:
            chocolates.pop()
        if first_cup <= 0:
            cups_of_milk.popleft()
    else:
        if last_chocolate == first_cup:
            milkshakes += 1
            chocolates.pop()
            cups_of_milk.popleft()
        else:
            chocolates[len(chocolates) - 1] -= 5
            cups_of_milk.append(cups_of_milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {print_func(chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {print_func(cups_of_milk)}")
else:
    print("Milk: empty")
