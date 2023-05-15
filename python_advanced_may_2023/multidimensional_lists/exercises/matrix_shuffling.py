def read_matrix(n_rows):
    current_matrix = []
    for _ in range(n_rows):
        row_data = input().split(" ")
        current_matrix.append(row_data)
    return current_matrix


def rows_check(matrix, current_row_1, current_row_2, matrix_rows):
    if current_row_1 < 0 or current_row_2 < 0:
        return False
    if current_row_1 >= matrix_rows and current_row_2 >= matrix_rows:
        return False
    return True


def cols_check(matrix, current_col_1, current_col_2, matrix_cols):
    if current_col_1 < 0 or current_col_2 < 0:
        return False
    if current_col_1 >= matrix_cols and current_col_2 >= matrix_cols:
        return False
    return True


def print_matrix_as_text(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))


rows, cols = [int(x) for x in input().split(" ")]
matrix = read_matrix(rows)

while True:
    command_args = input().split(" ")

    if command_args[0] == "END":
        break

    if command_args[0] == "swap" and len(command_args) == 5:
        row_1, row_2 = int(command_args[1]), int(command_args[3])
        col_1, col_2 = int(command_args[2]), int(command_args[4])

        if rows_check(matrix, row_1, row_2, rows) and cols_check(matrix, col_1, col_2, cols):
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            print_matrix_as_text(matrix)
        else:
            print("Invalid input!")

    else:
        print("Invalid input!")

