import os
from collections import deque

directory_name = input("Enter directory name for output files: ")

while True:
    command_args = input()

    if command_args == "End":
        break

    data = deque(x for x in command_args.split("-"))
    command, file_name, content, new_content = (
        data.popleft(), data.popleft(),
        data.popleft() if data else "", data.popleft() if data else ""
    )

    absolute_path = os.path.abspath(os.path.dirname(__file__))
    new_directory_path = os.path.join(absolute_path, directory_name)

    try:
        os.mkdir(new_directory_path)

    except FileExistsError:
        pass

    if command == "Create":
        with open(os.path.join(new_directory_path, file_name), "w") as file:
            pass

    elif command == "Add":
        with open(os.path.join(new_directory_path, file_name), "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        try:
            with open(os.path.join(new_directory_path, file_name), "r") as file:
                lines = file.read()
                lines = lines.replace(content, new_content)

            with open(os.path.join(new_directory_path, file_name), "w") as file:
                file.write(lines)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(os.path.join(new_directory_path, file_name))

        except FileNotFoundError:
            print("An error occurred")
