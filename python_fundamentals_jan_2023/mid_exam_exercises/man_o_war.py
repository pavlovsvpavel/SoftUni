def indices_check(lst, num):
    if 0 <= num <= len(lst) - 1:
        return True
    else:
        return False


pirate_ship = [int(x) for x in input().split(">")]
war_ship = [int(x) for x in input().split(">")]
MAX_HEALTH = int(input())
is_lost = False
while True:
    command_args = input().split(" ")
    command = command_args[0]

    if command == "Retire":
        break

    if command == "Fire":
        index = int(command_args[1])
        damage = int(command_args[2])
        if indices_check(war_ship, index):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                is_lost = True
                print("You won! The enemy ship has sunken.")
                break
    elif command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if indices_check(pirate_ship, start_idx) and indices_check(pirate_ship, end_idx):
            for idx in range(start_idx, end_idx + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    is_lost = True
                    print("You lost! The pirate ship has sunken.")
                    break
    elif command == "Repair":
        index = int(command_args[1])
        health = int(command_args[2])
        if indices_check(pirate_ship, index):
            pirate_ship[index] = min(pirate_ship[index] + health, MAX_HEALTH)
    elif command == "Status":
        sections_for_repair = [x for x in pirate_ship if x < MAX_HEALTH * 0.2]
        print(f"{len(sections_for_repair)} sections need repair.")

if not is_lost:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
