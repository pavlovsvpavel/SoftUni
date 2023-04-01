def index_validation(idx, lst):
    if 0 <= idx < len(lst):
        return True


count_commands = int(input())
houses = input().split(" ")
last_house_index = 0
for _ in range(count_commands):
    command_args = input().split(" ")
    command = command_args[0]

    if command == "Forward":
        steps = int(command_args[1])
        current_index = last_house_index + steps
        if index_validation(current_index, houses):
            houses.pop(current_index)
            last_house_index = current_index
    elif command == "Back":
        steps = int(command_args[1])
        current_index = last_house_index - steps
        if index_validation(current_index, houses):
            houses.pop(current_index)
            last_house_index = current_index
    elif command == "Gift":
        index = int(command_args[1])
        house_number = command_args[2]
        if index_validation(index, houses):
            houses.insert(index, house_number)
            last_house_index = index
    elif command == "Swap":
        house_1 = command_args[1]
        house_2 = command_args[2]
        if house_1 not in houses or house_2 not in houses:
            continue
        index_1 = houses.index(house_1)
        index_2 = houses.index(house_2)
        if index_validation(index_1, houses) and index_validation(index_2, houses):
            houses[index_1], houses[index_2] = houses[index_2], houses[index_1]

print(f"Position: {last_house_index}")
print(", ".join(houses))
