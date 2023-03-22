count_heroes = int(input())

MAX_HP = 100
MAX_MP = 200
heroes_collection = {}
for _ in range(count_heroes):
    hero, hit_points, mana_points = input().split(" ")
    heroes_collection[hero] = [int(hit_points), int(mana_points)]

while True:
    command = input()
    if command == "End":
        break

    command_args = command.split(" - ")
    hero_name = command_args[1]

    if command_args[0] == "CastSpell":
        needed_mana = int(command_args[2])
        spell_name = command_args[3]
        if heroes_collection[hero_name][1] >= needed_mana:
            heroes_collection[hero_name][1] -= needed_mana
            current_mp = heroes_collection[hero_name][1]
            print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command_args[0] == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]
        heroes_collection[hero_name][0] -= damage
        if heroes_collection[hero_name][0] > 0:
            current_hp = heroes_collection[hero_name][0]
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            heroes_collection.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command_args[0] == "Recharge":
        add_mp = int(command_args[2])
        current_mp = heroes_collection[hero_name][1]
        heroes_collection[hero_name][1] += add_mp
        if heroes_collection[hero_name][1] > MAX_MP:
            heroes_collection[hero_name][1] = min(current_mp + add_mp, MAX_MP)
            recovered_mp = MAX_MP - current_mp
        else:
            recovered_mp = add_mp
        print(f"{hero_name} recharged for {recovered_mp} MP!")
    elif command_args[0] == "Heal":
        add_hp = int(command_args[2])
        current_hp = heroes_collection[hero_name][0]
        heroes_collection[hero_name][0] += add_hp
        if heroes_collection[hero_name][0] > MAX_HP:
            heroes_collection[hero_name][0] = min(current_hp + add_hp, MAX_HP)
            recovered_hp = MAX_HP - current_hp
        else:
            recovered_hp = add_hp
        print(f"{hero_name} healed for {recovered_hp} HP!")

for name, values in heroes_collection.items():
    print(f"{name}\n  HP: {values[0]}\n  MP: {values[1]}")
