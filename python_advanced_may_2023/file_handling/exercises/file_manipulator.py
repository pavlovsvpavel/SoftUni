from os import remove
from collections import deque

while True:
    command_args = input()

    if command_args == "End":
        break

    data = deque(x for x in command_args.split("-"))
    command, file_name, content, new_content = (
        data.popleft(), data.popleft(),
        data.popleft() if data else "", data.popleft() if data else ""
    )

    if command == "Create":
        file = open(f"files/{file_name}", "w")
        file.close()

    elif command == "Add":
        with open(f"files/{file_name}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        try:
            with open(f"files/{file_name}", "r") as file:
                lines = file.read()
                lines = lines.replace(content, new_content)

            with open(f"files/{file_name}", "w") as file:
                file.write(lines)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            remove(f"files/{file_name}")

        except FileNotFoundError:
            print("An error occurred")
