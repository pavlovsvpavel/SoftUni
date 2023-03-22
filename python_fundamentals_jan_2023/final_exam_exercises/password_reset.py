password = input()
substring = ""
while True:
    command = input()
    if command == "Done":
        break

    command_args = command.split(" ")

    if command_args[0] == "TakeOdd":
        for idx, char in enumerate(password):
            if idx % 2 != 0:
                substring += char
        password = substring
        substring = ""
        print(password)
    elif command_args[0] == "Cut":
        index = int(command_args[1])
        length = int(command_args[2])
        for idx in range(length):
            substring += password[index + idx]
        password = password.replace(substring, "", 1)
        substring = ""
        print(password)
    elif command_args[0] == "Substitute":
        string_to_remove = command_args[1]
        string_to_add = command_args[2]
        if string_to_remove in password:
            password = password.replace(string_to_remove, string_to_add)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
