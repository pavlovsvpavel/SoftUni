from collections import deque

materials = [int(x) for x in input().split(" ")]
magic_levels = deque(int(x) for x in input().split(" "))

toys = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}
crafted_toys = {}
while materials and magic_levels:
    last_material = materials.pop()
    first_magic_level = magic_levels.popleft()
    current_magic_level = last_material * first_magic_level

    if last_material == 0 and first_magic_level == 0:
        continue
    if last_material == 0:
        magic_levels.appendleft(first_magic_level)
        continue
    if first_magic_level == 0:
        materials.append(last_material)
        continue

    if current_magic_level in toys.values():
        for toy, magic in toys.items():
            if current_magic_level == magic:
                crafted_toys[toy] = crafted_toys.get(toy, 0) + 1
    elif current_magic_level < 0:
        new_material = last_material + first_magic_level
        materials.append(new_material)
    else:
        last_material += 15
        materials.append(last_material)

if ("Doll" in crafted_toys.keys() and "Wooden train" in crafted_toys.keys()) or \
        ("Teddy bear" in crafted_toys.keys() and "Bicycle" in crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for k, v in sorted(crafted_toys.items()):
    print(f"{k}: {v}")
