from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    elements_sum = current_textile + current_medicament

    if elements_sum == 30:
        items["Patch"] += 1

    elif elements_sum == 40:
        items["Bandage"] += 1

    elif elements_sum == 100:
        items["MedKit"] += 1

    elif elements_sum > 100:
        items["MedKit"] += 1
        medicament = medicaments.pop() + elements_sum - 100
        medicaments.append(medicament)

    else:
        medicaments.append(current_medicament + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not medicaments:
    print("Medicaments are empty.")

else:
    print("Textiles are empty.")

for item_name, count in sorted(items.items(), key=lambda x: (-x[1], x[0])):
    if count > 0:
        print(f"{item_name} - {count}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")

if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")
