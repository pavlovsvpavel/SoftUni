def read_matrix_func():
    num_of_rows = int(input())
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(map(int, input().split(" ")))
        current_matrix.append(row_data)

    return current_matrix


def calc_primary_diagonal(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][i]

    return result


matrix = read_matrix_func()
print(calc_primary_diagonal(matrix))
