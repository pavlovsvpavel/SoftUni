from collections import deque


def leftovers(elements):
    result = []
    for el in elements:
        result.append(str(el))
    return " ".join(result)


cups = deque([int(x) for x in input().split(" ")])
bottles = [int(x) for x in input().split(" ")]
wasted_litters = 0
while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups[0]
    if current_bottle >= current_cup:
        wasted_litters += current_bottle - current_cup
        current_cup -= current_bottle
        if current_cup <= 0:
            cups.popleft()
    else:
        cups[0] -= current_bottle
        continue

if bottles:
    print(f"Bottles: {leftovers(bottles)}")
elif cups:
    print(f"Cups: {leftovers(cups)}")

print(f"Wasted litters of water: {wasted_litters}")
