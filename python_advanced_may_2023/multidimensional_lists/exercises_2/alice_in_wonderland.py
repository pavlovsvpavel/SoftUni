def indices_check(row_idx, col_idx, size):
    return 0 <= row_idx < size and 0 <= col_idx < size


def check_for_rabbit(matrix, row_idx, col_idx):
    if matrix[row_idx][col_idx] == "R":
        matrix[row_idx][col_idx] = "*"
        return False
    return True


matrix_size = int(input())
matrix = [input().split() for _ in range(matrix_size)]

alice_coords = ()
tea_bags = 0

moves = {
    "up": (-1, 0),
    "down": (+1, 0),
    "left": (0, -1),
    "right": (0, +1),
}

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "A":
            alice_coords = row, col
            matrix[row][col] = "*"

while tea_bags < 10:
    command = input()

    curr_row, curr_col = alice_coords[0] + moves[command][0], alice_coords[1] + moves[command][1]

    if not indices_check(curr_row, curr_col, matrix_size) or not check_for_rabbit(matrix, curr_row, curr_col):
        print("Alice didn't make it to the tea party.")
        break

    current_position = matrix[curr_row][curr_col]

    if current_position.isdigit():
        tea_bags += int(current_position)

    matrix[curr_row][curr_col] = "*"
    alice_coords = curr_row, curr_col
    
if tea_bags >= 10:
    print(f"She did it! She went to the party.")

[print(*inner_list, sep=" ") for inner_list in matrix]
