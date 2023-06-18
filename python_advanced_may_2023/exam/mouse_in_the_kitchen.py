def out_of_matrix(matrix, row, col):
    return row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row])


def find_mouse_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "M":
                return i, j


def count_all_cheese(matrix):
    cheeses = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "C":
                cheeses += 1

    return cheeses


rows, cols = [int(x) for x in input().split(",")]
board = [list(input()) for _ in range(rows)]

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

mouse_row, mouse_col = find_mouse_pos(board)
board[mouse_row][mouse_col] = "*"

total_cheeses = count_all_cheese(board)
found_cheeses = 0

while True:
    command = input()

    if found_cheeses == total_cheeses:
        print("Happy mouse! All the cheese is eaten, good night!")
        break

    if command == "danger":
        print("Mouse will come back later!")
        break

    current_row, current_col = directions[command](mouse_row, mouse_col)

    if out_of_matrix(board, current_row, current_col):
        print("No more cheese for tonight!")
        break

    if board[current_row][current_col] == "@":
        continue

    mouse_row, mouse_col = current_row, current_col

    if board[current_row][current_col] == "C":
        found_cheeses += 1

    if board[current_row][current_col] == "T":
        board[mouse_row][mouse_col] = "M"
        print("Mouse is trapped!")
        break

    board[current_row][current_col] = "*"

board[mouse_row][mouse_col] = "M"

[print(*row, sep="") for row in board]
