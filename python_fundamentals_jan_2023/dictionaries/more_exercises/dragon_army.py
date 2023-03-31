count_dragons = int(input())
DAMAGE = 45  # default value, if "null" is given in the input
HEALTH = 250  # default value, if "null" is given in the input
ARMOR = 10  # default value, if "null" is given in the input

all_dragons = {}
for _ in range(count_dragons):
    line = input()
    line_args = line.split(" ")
    dragon_type = line_args[0]
    name = line_args[1]

    for stat in line_args:
        if stat == "null":
            index = line_args.index(stat)
            if index == 2:
                line_args[index] = str(DAMAGE)
            elif index == 3:
                line_args[index] = str(HEALTH)
            elif index == 4:
                line_args[index] = str(ARMOR)

    damage = int(line_args[2])
    health = int(line_args[3])
    armor = int(line_args[4])

    all_dragons[dragon_type] = all_dragons.get(dragon_type, {})
    all_dragons[dragon_type][name] = all_dragons[dragon_type].get(name, {})
    all_dragons[dragon_type][name]["damage"], all_dragons[dragon_type][name]["health"], \
        all_dragons[dragon_type][name]["armor"] = damage, health, armor

for current_type, names in all_dragons.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    count_names = 0
    for current_name, stats in names.items():
        total_damage += stats["damage"]
        total_health += stats["health"]
        total_armor += stats["armor"]
        count_names += 1
    print(f"{current_type}::({total_damage/count_names:.2f}/{total_health/count_names:.2f}/"
          f"{total_armor/count_names:.2f})")

    for current_name, stats in sorted(names.items(), key=lambda x: x[0]):
        print(f"-{current_name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
