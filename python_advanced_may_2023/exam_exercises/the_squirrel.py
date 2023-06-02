def indices_validation(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def check_current_pos(matrix, row, col):
    hazelnuts = 0
    trap = False
    if matrix[row][col] == "h":
        hazelnuts += 1
        matrix[row][col] = "*"
    elif matrix[row][col] == "t":
        trap = True

    return hazelnuts, trap


rows = int(input())
commands = input().split(", ")
field = [list(input()) for x in range(rows)]

total_hazelnuts = 0
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, 0),
}

squirrel_start_pos = 0, 0
for i in range(rows):
    for j in range(rows):
        if field[i][j] == "s":
            squirrel_start_pos = i, j
            break

for command in commands:
    current_row, current_col = (
        squirrel_start_pos[0] + directions[command][0],
        squirrel_start_pos[1] + directions[command][1]
    )

    if not indices_validation(field, current_row, current_col):
        print("The squirrel is out of the field.")
        break

    collected_hazelnuts, traps = check_current_pos(field, current_row, current_col)
    total_hazelnuts += collected_hazelnuts

    if traps:
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    squirrel_start_pos = current_row, current_col

    if total_hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {total_hazelnuts}")
