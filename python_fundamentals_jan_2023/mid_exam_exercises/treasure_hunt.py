def items_length(lst):
    item_lengths = [len(x) for x in lst]
    sum_of_letters = sum(item_lengths)
    result = sum_of_letters / len(lst)
    return f"{result:.2f}"


treasure_chest = [x for x in input().split("|")]

while True:
    command_args = input().split(" ")
    command = command_args[0]

    if command == "Yohoho!":
        break

    if command == "Loot":
        for idx in range(1, len(command_args)):
            if command_args[idx] in treasure_chest:
                continue
            else:
                treasure_chest.insert(0, command_args[idx])
    elif command == "Drop":
        index = int(command_args[1])
        if 0 < index <= len(treasure_chest):
            item = treasure_chest.pop(index)
            treasure_chest.append(item)
    elif command == "Steal":
        index = int(command_args[1])
        stolen_items = []
        if index > len(treasure_chest):
            index = len(treasure_chest)
        for idx in range(index):
            item = treasure_chest.pop()
            stolen_items.insert(0, item)
        print(", ".join(stolen_items))

if treasure_chest:
    print(f"Average treasure gain: {items_length(treasure_chest)} pirate credits.")
else:
    print("Failed treasure hunt.")
