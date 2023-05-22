def indices_check(row_idx, col_idx):
    return 0 <= row_idx < SIZE and 0 <= col_idx < SIZE


def movements(matrix, bunny, all_moves, current_direction):
    eggs = 0
    current_path = []
    current_row = bunny[0] + all_moves[current_direction][0]
    current_col = bunny[1] + all_moves[current_direction][1]

    while True:
        if not indices_check(current_row, current_col) or matrix[current_row][current_col] == "X":
            break
        eggs += int(matrix[current_row][current_col])
        current_path.append([current_row, current_col])
        current_row += all_moves[current_direction][0]
        current_col += all_moves[current_direction][1]

    return eggs, current_path


def print_func(directions_eggs, max_eggs):
    curr_direction, curr_path = directions_eggs[max_eggs]
    print(curr_direction)
    [print(coordinates) for coordinates in curr_path]
    print(max_eggs)


SIZE = int(input())
matrix = []
bunny_coords, traps = (), []

for row in range(SIZE):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_coords = (row, matrix[row].index("B"))
    traps.append(matrix[row].count("X"))

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
max_total_eggs = 0
all_paths = {}

for move in moves.keys():
    total_eggs, path = movements(matrix, bunny_coords, moves, move)

    if total_eggs >= max_total_eggs:
        max_total_eggs = total_eggs
        all_paths[total_eggs] = (move, path)

print_func(all_paths, max_total_eggs)
