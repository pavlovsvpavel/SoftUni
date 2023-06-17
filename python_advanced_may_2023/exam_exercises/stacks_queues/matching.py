from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches = 0
while males and females:

    current_male = males.pop()
    current_female = females.popleft()

    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_female <= 0:
        males.append(current_male)
        continue

    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_male == current_female:
        matches += 1
    else:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")
else:
    print(f"Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print(f"Females left: none")
