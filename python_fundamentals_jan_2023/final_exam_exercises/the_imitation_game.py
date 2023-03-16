message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command_args = command.split("|")

    if command_args[0] == "Move":
        number_of_letters = int(command_args[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif command_args[0] == "Insert":
        index = int(command_args[1])
        value = command_args[2]
        message = message[:index] + value + message[index:]
    elif command_args[0] == "ChangeAll":
        searched_value = command_args[1]
        replacing_value = command_args[2]
        message = message.replace(searched_value, replacing_value)

print(f"The decrypted message is: {message}")

