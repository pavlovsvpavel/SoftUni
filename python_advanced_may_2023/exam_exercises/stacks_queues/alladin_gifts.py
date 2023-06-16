from collections import deque


def gifts_crafting():

    if 100 <= magic <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= magic <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= magic <= 399:
        gifts["Gold"] += 1
    elif 400 <= magic <= 499:
        gifts["Diamond Jewellery"] += 1


materials = deque(int(x) for x in input().split())
levels = deque(int(x) for x in input().split())


gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}

while materials and levels:
    current_material = materials.pop()
    current_level = levels.popleft()

    magic = current_material + current_level

    if magic < 100 and magic % 2 == 0:
        magic = current_material * 2 + current_level * 3

    elif magic < 100 and magic % 2 != 0:
        magic = current_material * 2 + current_level * 2

    elif magic > 499:
        magic = current_material / 2 + current_level / 2

    if magic < 100 or magic > 499:
        continue

    gifts_crafting()

if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
if levels:
    print(f'Magic left: {", ".join(map(str, levels))}')

for gift, qty in sorted(gifts.items(), reverse=False):
    if qty > 0:
        print(f"{gift}: {qty}")
