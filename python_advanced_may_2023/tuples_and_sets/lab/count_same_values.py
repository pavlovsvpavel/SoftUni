numbers = tuple(map(lambda x: float(x), input().split(" ")))

occurrences = {}
for number in numbers:
    if number not in occurrences:
        occurrences[number] = 0

    occurrences[number] += 1

for key, value in occurrences.items():
    print(f"{key} - {value} times")

