def check_index(lst, idx):
    if 0 <= idx <= len(lst) - 1:
        return True
    else:
        return False


coffee_list = input().split(" ")
count_commands = int(input())

for _ in range(count_commands):
    command_args = input().split(" ")
    command = command_args[0]
    if command == "Include":
        item = command_args[1]
        coffee_list.append(item)
    elif command == "Remove":
        index = int(command_args[2])
        if check_index(coffee_list, index):
            if "first" in command_args[1]:
                for i in range(index):
                    coffee_list.pop(0)
            elif "last" in command_args[1]:
                for i in range(index - 1, - 1, - 1):
                    coffee_list.pop(-1)
    elif command == "Prefer":
        index_1 = int(command_args[1])
        index_2 = int(command_args[2])
        if check_index(coffee_list, index_1) and check_index(coffee_list, index_2):
            coffee_list[index_1], coffee_list[index_2] = coffee_list[index_2], coffee_list[index_1]
    elif command == "Reverse":
        coffee_list.reverse()

print("Coffees:")
print(" ".join(coffee_list))
