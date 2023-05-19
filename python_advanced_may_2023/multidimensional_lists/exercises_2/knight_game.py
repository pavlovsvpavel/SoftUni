def check_for_knight(matrix, row, col):
    attacks = 0
    if matrix[row][col] == "K":
        attacks += 1

    return attacks


def indices_check(matrix, row_idx, col_idx):
    if 0 <= row_idx < len(matrix) and 0 <= col_idx < len(matrix[0]):
        return True
    return False


rows = int(input())
matrix = [list(input()) for _ in range(rows)]

movements = {
    "up_left": lambda x, y: (x - 2, y + 1),
    "up_right": lambda x, y: (x - 2, y - 1),
    "left_up": lambda x, y: (x - 1, y - 2),
    "left_down": lambda x, y: (x + 1, y - 2),
    "right_up": lambda x, y: (x - 1, y + 2),
    "right_down": lambda x, y: (x + 1, y + 2),
    "down_left": lambda x, y: (x + 2, y - 1),
    "down_right": lambda x, y: (x + 2, y + 1),
}

removed_knights = 0
while True:
    max_attacks = 0
    knight_max_attacks_pos = []

    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == "K":
                knight_row, knight_col = i, j
                current_attacks = 0

                for move, directions in movements.items():
                    current_row, current_col = movements[move](knight_row, knight_col)

                    if indices_check(matrix, current_row, current_col):
                        current_attacks += check_for_knight(matrix, current_row, current_col)

                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_max_attacks_pos = [knight_row, knight_col]

    if knight_max_attacks_pos:
        removed_knights += 1
        matrix[knight_max_attacks_pos[0]][knight_max_attacks_pos[1]] = "0"
    else:
        break

print(removed_knights)
