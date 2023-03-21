text = input()

while True:
    command = input()

    if command == "Reveal":
        break

    command_args = command.split(":|:")
    flag = False
    if command_args[0] == "InsertSpace":
        index = int(command_args[1])
        text = text[:index] + " " + text[index:]
    elif command_args[0] == "Reverse":
        substring = command_args[1]
        reversed_substring = substring[::-1]
        if substring in text:
            text = text.replace(substring, "", 1)
            text += reversed_substring
        else:
            flag = True
            print("error")
    elif command_args[0] == "ChangeAll":
        old_string = command_args[1]
        new_string = command_args[2]
        text = text.replace(old_string, new_string)
    if not flag:
        print(text)

print(f"You have a new text message: {text}")
