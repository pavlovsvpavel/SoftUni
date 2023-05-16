def read_matrix_func():
    num_of_rows, num_of_columns = map(int, input().split(", "))
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(map(int, input().split(", ")))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()
max_sum = float("-inf")
submatrix = []
for row in range(len(matrix) - 1):
    for col in range(len(matrix[0]) - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        below_element = matrix[row + 1][col]
        diagonal_element = matrix[row + 1][col + 1]
        sum_of_elements = current_element + next_element + below_element + diagonal_element

        if max_sum < sum_of_elements:
            max_sum = sum_of_elements
            submatrix = [[current_element, next_element], [below_element, diagonal_element]]

print(*submatrix[0])
print(*submatrix[1])
print(max_sum)
