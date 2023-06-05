def movements(row, col):
    directions = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "right": lambda x, y: (x, y + 1),
        "left": lambda x, y: (x, y - 1),
    }
    row, col = directions[direction](row, col)

    return row, col


matrix = [input().split() for x in range(6)]
start_pos = input().strip("(").strip(")").split(", ")

row, col = int(start_pos[0]), int(start_pos[1])

while True:
    command, *data = [x if x else "" for x in input().split(", ")]

    if command == "Stop":
        break

    direction = data[0]

    if command == "Create":
        value = data[1]
        row, col = movements(row, col)

        if matrix[row][col] == ".":
            matrix[row][col] = value

    elif command == "Update":
        value = data[1]
        row, col = movements(row, col)

        if matrix[row][col] != ".":
            matrix[row][col] = value

    elif command == "Delete":
        row, col = movements(row, col)

        if matrix[row][col] != ".":
            matrix[row][col] = "."

    elif command == "Read":
        row, col = movements(row, col)

        if matrix[row][col] != ".":
            print(matrix[row][col])

[print(*inner_list, sep=" ") for inner_list in matrix]
