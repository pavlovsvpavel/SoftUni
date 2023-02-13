rooms = input().split("|")
init_health = 100
bitcoins = 0
is_valid = True
current_health = init_health
for room in range(len(rooms)):
    command_args = rooms[room].split(" ")
    if command_args[0] == "potion":
        healing_pts = int(command_args[1])
        current_health += healing_pts
        if current_health > init_health:
            diff = abs(init_health - current_health)
            healed_pts = abs(diff - healing_pts)
            current_health = min(init_health, current_health)
        else:
            healed_pts = healing_pts
        print(f"You healed for {healed_pts} hp.")
        print(f"Current health: {current_health} hp.")
    elif command_args[0] == "chest":
        found_bitcoins = int(command_args[1])
        bitcoins += found_bitcoins
        print(f"You found {found_bitcoins} bitcoins.")
    else:
        monster = command_args[0]
        monster_attack = int(command_args[1])
        current_health -= monster_attack
        if current_health > 0:
            print(f"You slayed {monster}.")
        else:
            is_valid = False
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room + 1}")
            break

if is_valid:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")

