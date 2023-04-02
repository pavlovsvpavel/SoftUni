def check_indices(idx_1, idx_2, txt):
    if 0 <= idx_1 < len(txt) and 0 <= idx_2 < len(txt):
        return True


message = input()

while True:
    command_args = input()

    if command_args == "Finish":
        break

    command = command_args.split(" ")

    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        message = message.replace(current_char, new_char)
        print(message)
    elif command[0] == "Cut":
        start_idx = int(command[1])
        end_idx = int(command[2])
        if check_indices(start_idx, end_idx, message):
            message = message[:start_idx] + message[end_idx + 1:]
            print(message)
        else:
            print("Invalid indices!")
    elif command[0] == "Make":
        change_case = command[1]
        if change_case == "Upper":
            message = message.upper()
        else:
            message = message.lower()
        print(message)
    elif command[0] == "Check":
        substring = command[1]
        if substring in message:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif command[0] == "Sum":
        start_idx = int(command[1])
        end_idx = int(command[2])
        sum_of_chars = 0
        if check_indices(start_idx, end_idx, message):
            for el in range(start_idx, end_idx + 1):
                char = message[el]
                sum_of_chars += ord(char)
            print(sum_of_chars)
        else:
            print("Invalid indices!")
