main_string = input()

while True:
    command = input()

    if command == "Travel":
        break

    command_args = command.split(":")

    if command_args[0] == "Add Stop":
        index = int(command_args[1])
        new_string = command_args[2]
        if 0 <= index < len(main_string):
            main_string = main_string[:index] + new_string + main_string[index:]
    elif command_args[0] == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if 0 <= start_index < len(main_string) and 0 <= end_index < len(main_string):
            main_string = main_string[:start_index] + main_string[end_index + 1:]
    elif command_args[0] == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]
        if old_string in main_string:
            main_string = main_string.replace(old_string, new_string)

    print(main_string)

print(f"Ready for world tour! Planned stops: {main_string}")
