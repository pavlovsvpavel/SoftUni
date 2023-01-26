events_list = input().split("|")

coins = 100
energy = 100

current_event = []
flag = True

for event in events_list:
    current_event = event.split("-")
    num_in_event = int(current_event[1])

    if "rest" in current_event:
        if 100 - energy < num_in_event:
            num_in_event = 100 - energy

        energy += num_in_event

        print(f"You gained {num_in_event} energy.")
        print(f"Current energy: {energy}.")

    elif "order" in current_event:
        if energy >= 30:
            energy -= 30
            coins += num_in_event
            print(f"You earned {num_in_event} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if num_in_event <= coins:
            coins -= num_in_event
            print(f"You bought {current_event[0]}.")
        else:
            print(f"Closed! Cannot afford {current_event[0]}.")
            flag = False
            break

if flag:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

