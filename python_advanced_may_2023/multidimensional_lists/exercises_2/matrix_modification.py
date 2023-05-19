def indices_check(matrix, row_idx, col_idx):
    if 0 <= row_idx < len(matrix) and 0 <= col_idx < len(matrix[0]):
        return True
    return print("Invalid coordinates")


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command, *info = [int(x) if x.lstrip("-").isdigit() else x for x in input().split()]

    if command == "END":
        break

    current_row = info[0]
    current_col = info[1]
    value = info[2]

    if command == "Add":
        if indices_check(matrix, current_row, current_col):
            matrix[current_row][current_col] += value

    elif command == "Subtract":
        if indices_check(matrix, current_row, current_col):
            matrix[current_row][current_col] -= value

[print(*inner_list, sep=" ") for inner_list in matrix]
