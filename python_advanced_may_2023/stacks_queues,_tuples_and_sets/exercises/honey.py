from collections import deque


def calculations(symbol, matched_bee, matched_nectar):
    result = 0
    if symbol == "+":
        result = matched_bee + matched_nectar
    elif symbol == "-":
        result = matched_bee - matched_nectar
    elif symbol == "*":
        result = matched_bee * matched_nectar
    elif symbol == "/":
        if matched_nectar == 0:
            result = 0
        else:
            result = matched_bee / matched_nectar
    return abs(result)


bees = deque(int(x) for x in input().split(" "))
nectar = [int(x) for x in input().split(" ")]
symbols = deque(input().split(" "))

total_honey = 0
while len(bees) > 0 and len(nectar) > 0:
    first_bee = bees[0]
    last_nectar = nectar[-1]

    if last_nectar >= first_bee:
        current_symbol = symbols.popleft()
        total_honey += calculations(current_symbol, first_bee, last_nectar)
        bees.popleft()
        nectar.pop()
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
