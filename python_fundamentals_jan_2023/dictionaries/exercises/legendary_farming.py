legendary_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
items = ["Shadowmourne", "Valanyr", "Dragonwrath"]
junk_materials = {}
MAX_SCORE = 250
is_winner = False
while not is_winner:
    materials = input().lower().split(" ")
    for index in range(0, len(materials), 2):
        item = materials[index + 1]
        quantity = materials[index]
        if item in legendary_materials.keys():
            legendary_materials[item] += int(quantity)
            if max(legendary_materials.values()) >= MAX_SCORE:
                legendary_materials[item] += - MAX_SCORE
                is_winner = True
                index = list(legendary_materials.keys()).index(item)
                print(f"{items[index]} obtained!")
                break
        elif item in junk_materials.keys():
            junk_materials[item] += int(quantity)
        else:
            junk_materials[item] = 0
            junk_materials[item] += int(quantity)

for item, quantity in legendary_materials.items():
    print(f"{item}: {quantity}")
for item, quantity in junk_materials.items():
    print(f"{item}: {quantity}")
