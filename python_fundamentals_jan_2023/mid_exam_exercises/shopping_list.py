def check_item(lst, product):
    for idx in range(len(lst)):
        if lst[idx] == product:
            return idx

    return -1


shopping_list = input().split("!")
while True:
    command_args = input()

    if command_args == "Go Shopping!":
        break

    commands = command_args.split(" ")
    current_command = commands[0]
    item = commands[1]

    if current_command == "Urgent":
        if check_item(shopping_list, item) == - 1:
            shopping_list.insert(0, item)
    elif current_command == "Unnecessary":
        if check_item(shopping_list, item) != - 1:
            shopping_list.remove(item)
    elif current_command == "Correct":
        new_item = commands[2]
        if check_item(shopping_list, item) != - 1:
            shopping_list.insert(check_item(shopping_list, item), new_item)
            shopping_list.remove(item)
    elif current_command == "Rearrange":
        if check_item(shopping_list, item) != - 1:
            shopping_list.remove(item)
            shopping_list.append(item)

print(", ".join(shopping_list))
