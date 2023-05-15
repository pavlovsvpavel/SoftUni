def read_matrix_func():
    num_of_rows, num_of_columns = map(int, input().split(", "))
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(map(int, input().split(", ")))
        current_matrix.append(row_data)

    return current_matrix


def sum_of_submatrix(matrix):
    result = 0
    for i in range(3):
        for j in range(3):
            result += matrix[i][j]


matrix = read_matrix_func()
submatrix_size = 2
sum_of_submatrix(matrix)

