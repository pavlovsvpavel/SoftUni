def read_matrix():
    rows, cols = [int(x) for x in input().split(" ")]
    current_matrix = []
    for _ in range(rows):
        row_data = list(input().split(" "))
        current_matrix.append(row_data)

    return current_matrix


def indexes_check(matrix, current_row, current_col):
    if current_row + 1 >= len(matrix) or current_col + 1 >= len(matrix[current_row]):
        return False
    return True


def submatrix_data(matrix, size, current_row, current_col):
    submatrix_elements = []
    for row_index in range(current_row, current_row + size):
        for col_index in range(current_col, current_col + size):
            submatrix_elements.append(matrix[row_index][col_index])

    return submatrix_elements


def check_identical_chars(lst):
    lst = set(lst)
    if len(lst) == 1:
        return True
    return False


matrix = read_matrix()
size_of_submatrix = 2
total_square_matrices = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if not indexes_check(matrix, row, col):
            break
        submatrix_chars = submatrix_data(matrix, size_of_submatrix, row, col)
        if check_identical_chars(submatrix_data(matrix, size_of_submatrix, row, col)):
            total_square_matrices += 1

print(total_square_matrices)
