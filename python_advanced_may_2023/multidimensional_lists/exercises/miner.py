def indices_check(matrix, row_idx, col_idx, move):
    movements = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "right": lambda x, y: (x, y + 1),
        "left": lambda x, y: (x, y - 1),
    }
    row_idx, col_idx = movements[move](row_idx, col_idx)

    if row_idx < 0 or col_idx < 0 or row_idx >= len(matrix) or col_idx >= len(matrix[0]):
        return False
    return row_idx, col_idx


def find_coal(matrix, row_idx, col_idx):
    if matrix[row_idx][col_idx] == "c":
        return True


def find_exit(matrix, row_idx, col_idx):
    if matrix[row_idx][col_idx] == "e":
        print(f"Game over! ({row_idx}, {col_idx})")
        return True


field_size = int(input())
commands = input().split(" ")

field = []
cases = []
for _ in range(field_size):
    row_data = input().split(" ")
    field.append(row_data)

current_row, current_col = (0, 0)
for i in range(field_size):
    for j in range(field_size):
        if field[i][j] == "s":
            current_row, current_col = i, j
            break

total_coals = len([element for row in field for element in row if element == "c"])

collected_coals = 0
for command in commands:
    if not indices_check(field, current_row, current_col, command):
        continue

    current_row, current_col = indices_check(field, current_row, current_col, command)

    if find_coal(field, current_row, current_col):
        collected_coals += 1
        field[current_row][current_col] = "*"

    if collected_coals == total_coals:
        print(f"You collected all coal! {current_row, current_col}")
        break

    if find_exit(field, current_row, current_col):
        break

else:
    print(f"{total_coals - collected_coals} pieces of coal left. {current_row, current_col}")
