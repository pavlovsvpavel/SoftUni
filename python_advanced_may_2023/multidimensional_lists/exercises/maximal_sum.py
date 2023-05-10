import numpy as np

def read_matrix():
    rows, cols = [int(x) for x in input().split(" ")]
    current_matrix = []
    for _ in range(rows):
        row_data = list(map(int, input().split(" ")))
        current_matrix.append(row_data)
    return current_matrix


def indexes_check(matrix, current_row, current_col):
    if current_row + 2 >= len(matrix) or current_col + 2 >= len(matrix[current_row]):
        return False
    return True


def submatrix_data(matrix, size, current_row, current_col):
    data = []
    for i in range(current_row, current_row + size):
        for j in range(current_col, current_col + size):
            data.append(matrix[i][j])
    return data


# def print_matrix(numbers, n):
#     result = ''
#     for i in range(len(numbers)):
#         result += f"{numbers[i]} "
#         if (i + 1) % n == 0:
#             result += '\n'
#     return result


def print_matrix2(numbers, n):
    result = ""
    arr = np.array(numbers)
    table = arr.reshape(n, n)
    for line in table:
        result += f'{" ".join(map(str, line))}\n'
    return result


matrix = read_matrix()
submatrix_size = 3
max_submatrix_sum = float("-inf")
max_submatrix_elements = []
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if not indexes_check(matrix, row, col):
            break
        submatrix_elements = submatrix_data(matrix, submatrix_size, row, col)
        submatrix_sum = sum(submatrix_elements)
        if submatrix_sum > max_submatrix_sum:
            max_submatrix_sum = submatrix_sum
            max_submatrix_elements = submatrix_elements

print(f"Sum = {max_submatrix_sum}")
# print(print_matrix(max_submatrix_elements, submatrix_size))
print(print_matrix2(max_submatrix_elements, submatrix_size))
