from collections import deque

caffeine = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

MAX_CAFFEINE = 300
total_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()
    result = current_caffeine * current_drink

    if result + total_caffeine <= MAX_CAFFEINE:
        total_caffeine += result
    else:
        energy_drinks.append(current_drink)

        if total_caffeine - 30 <= 0:
            continue
        total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
