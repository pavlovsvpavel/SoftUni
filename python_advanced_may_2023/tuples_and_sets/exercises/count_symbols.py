text = input()

elements_occurrences = {}
for el in text:
    if el not in elements_occurrences:
        elements_occurrences[el] = 0

    elements_occurrences[el] += 1

for char, value in sorted(elements_occurrences.items()):
    print(f"{char}: {value} time/s")
