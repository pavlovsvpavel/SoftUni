towns = {}
while True:
    data = input()
    if data == "Sail":
        break
    split_data = data.split("||")
    town = split_data[0]
    people = int(split_data[1])
    gold = int(split_data[2])

    if town not in towns:
        towns[town] = {"population": people, "treasure": gold}
    else:
        towns[town]["population"] += people
        towns[town]["treasure"] += gold

while True:
    data = input()
    if data == "End":
        break

    command_args = data.split("=>")
    command = command_args[0]
    town = command_args[1]

    if command == "Plunder":
        people = int(command_args[2])
        gold = int(command_args[3])
        towns[town]["population"] -= people
        towns[town]["treasure"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if towns[town]["population"] <= 0 or towns[town]["treasure"] <= 0:
            towns.pop(town)
            print(f"{town} has been wiped off the map!")
    elif command == "Prosper":
        gold = int(command_args[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        else:
            towns[town]["treasure"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['treasure']} gold.")

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town, value in towns.items():
        print(f"{town} -> Population: {value['population']} citizens, Gold: {value['treasure']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
