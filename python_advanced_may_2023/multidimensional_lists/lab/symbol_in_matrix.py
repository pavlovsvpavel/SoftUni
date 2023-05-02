def read_matrix_func():
    num_of_rows = int(input())
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(input())
        current_matrix.append(row_data)

    return current_matrix


def check_for_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == symbol:
                return row, col


matrix = read_matrix_func()
special_symbol = input()

if check_for_symbol(matrix, special_symbol):
    print(check_for_symbol(matrix, special_symbol))
else:
    print(f"{special_symbol} does not occur in the matrix")
