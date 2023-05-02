def read_matrix_func():
    num_of_rows = int(input())
    current_matrix = []
    for row in range(num_of_rows):
        row_data = list(map(int, input().split(", ")))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()
flattened_matrix = []

for row in matrix:
    for num in row:
        flattened_matrix.append(num)

print(flattened_matrix)
