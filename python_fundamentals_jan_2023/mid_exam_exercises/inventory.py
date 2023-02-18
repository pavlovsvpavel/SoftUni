inventory = [x for x in input().split(", ")]

while True:
    command_args = input().split(" - ")
    command = command_args[0]

    if command == "Craft!":
        break

    item = command_args[1]
    if command == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif command == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif command == "Combine Items":
        items = [x for x in item.split(":")]
        item = items[0]
        new_item = items[1]
        if item in inventory:
            index = inventory.index(item)
            inventory.insert(index + 1, new_item)
    elif command == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(", ".join(inventory))
