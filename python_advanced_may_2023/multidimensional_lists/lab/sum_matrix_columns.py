def read_matrix_func():
    num_of_rows, num_of_columns = map(int, input().split(", "))
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(map(int, input().split(" ")))
        current_matrix.append(row_data)

    return current_matrix


def sum_of_column_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for i in range(cols):
        sum_of_elements = 0
        for j in range(rows):
            sum_of_elements += matrix[j][i]
        result.append(sum_of_elements)

    return result


matrix = read_matrix_func()
for num in sum_of_column_elements(matrix):
    print(num)
