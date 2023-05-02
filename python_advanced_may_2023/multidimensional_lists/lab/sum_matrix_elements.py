def read_matrix_func():
    num_of_rows, num_of_columns = map(int, input().split(", "))
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(map(int, input().split(", ")))
        current_matrix.append(row_data)

    return current_matrix


def sum_elements(matrix):
    sum_of_elements = 0
    for i in range(len(matrix)):
        for j in matrix[i]:
            sum_of_elements += j

    return sum_of_elements


matrix = read_matrix_func()
print(sum_elements(matrix))
print(matrix)
