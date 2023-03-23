activation_key = input()

while True:
    command_args = input()
    if command_args == "Generate":
        break

    command = command_args.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        command_change_case = command[1]
        start_idx = int(command[2])
        end_idx = int(command[3])
        if command_change_case == "Upper":
            activation_key = activation_key[:start_idx] + \
                             activation_key[start_idx:end_idx].upper() + \
                             activation_key[end_idx:]
        else:
            activation_key = activation_key[:start_idx] + \
                             activation_key[start_idx:end_idx].lower() + \
                             activation_key[end_idx:]
        print(activation_key)
    elif command[0] == "Slice":
        start_idx = int(command[1])
        end_idx = int(command[2])
        activation_key = activation_key[:start_idx] + activation_key[end_idx:]
        print(activation_key)
print(f"Your activation key is: {activation_key}")
