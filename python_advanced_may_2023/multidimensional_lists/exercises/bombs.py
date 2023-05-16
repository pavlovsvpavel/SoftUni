def print_matrix_as_text(matrix):
    for i in matrix:
        print(" ".join(map(str, i)))


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
bombs_coordinates = input().split(" ")

functions = {
    "up_left": lambda x, y: (x - 1, y - 1),
    "up": lambda x, y: (x - 1, y),
    "up_right": lambda x, y: (x - 1, y + 1),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1),
    "down_left": lambda x, y: (x + 1, y - 1),
    "down": lambda x, y: (x + 1, y),
    "down_right": lambda x, y: (x + 1, y + 1),
}

for bomb in bombs_coordinates:
    row, col = map(int, bomb.split(","))

    if matrix[row][col] <= 0:
        continue

    damage = matrix[row][col]
    matrix[row][col] = 0
    
    for direction in functions.keys():
        current_cell_coord = functions[direction](row, col)
        current_row = current_cell_coord[0]
        current_col = current_cell_coord[1]

        if current_row < 0 or current_col < 0 or \
                current_row >= rows or current_col >= rows:
            continue

        current_cell = matrix[current_row][current_col]

        if current_cell <= 0:
            continue

        matrix[current_row][current_col] -= damage

flattened_matrix = [element for row in matrix for element in row]
alive_cells = [el for el in flattened_matrix if el > 0]
sum_alive_cells = sum(alive_cells)

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum_alive_cells}")
print_matrix_as_text(matrix)
