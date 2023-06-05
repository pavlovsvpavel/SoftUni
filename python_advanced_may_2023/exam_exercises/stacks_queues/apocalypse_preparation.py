from collections import deque


def check_for_match(resources, dictionary):
    for item, res in dictionary.items():
        res_needed = dictionary[item][0]

        if resources == res_needed:
            return item, 1

        elif resources > res_needed and item == "MedKit":
            diff = resources - res_needed
            return item, diff

    return 0, 0


textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

items = {
    "Patch": [30, 0],
    "Bandage": [40, 0],
    "MedKit": [100, 0],
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    elements_sum = current_textile + current_medicament

    item_name, value = check_for_match(elements_sum, items)

    if value == 1:
        items[item_name][1] += value

    elif value > 1:
        items[item_name][1] += 1
        medicaments.append(medicaments.pop() + value)

    else:
        medicaments.append(current_medicament + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not medicaments:
    print("Medicaments are empty.")

else:
    print("Textiles are empty.")

for item_name, values in sorted(items.items(), key=lambda x: (-x[1][1], x[0])):
    count = values[1]
    if count > 0:
        print(f"{item_name} - {count}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
