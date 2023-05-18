def indices_check(n_1, n_2, matrix_range):
    if n_1 < 0 or n_2 < 0:
        return False
    if n_1 >= matrix_range and n_2 >= matrix_range:
        return False
    return True


rows, cols = [int(x) for x in input().split(" ")]
matrix = [input().split() for _ in range(rows)]

while True:
    command_args = input().split(" ")

    if command_args[0] == "END":
        break

    if command_args[0] == "swap" and len(command_args) == 5:
        row_1, row_2 = int(command_args[1]), int(command_args[3])
        col_1, col_2 = int(command_args[2]), int(command_args[4])

        if indices_check(row_1, row_2, rows) and indices_check(col_1, col_2, cols):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            [print(*inner_list, sep=" ") for inner_list in matrix]
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")
