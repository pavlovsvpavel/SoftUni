def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def set_queen(row, col, board, rows, cols, lef_diag, right_diag):
    board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    lef_diag.add(row - col)
    right_diag.add(row + col)


def can_place_queen(row, col, board, rows, cols, lef_diag, right_diag):
    if row in rows:
        return False
    if col in cols:
        return False
    if (row - col) in lef_diag:
        return False
    if (row + col) in right_diag:
        return False
    return True


def remove_queen(row, col, board, rows, cols, lef_diag, right_diag):
    board[row][col] = "-"
    rows.remove(row)
    cols.remove(col)
    lef_diag.remove(row - col)
    right_diag.remove(row + col)


def put_queen(row, board, rows, cols, lef_diag, right_diag):
    if row == 8:
        print_board(board)
        return
    for col in range(8):
        if can_place_queen(row, col, board, rows, cols, lef_diag, right_diag):
            set_queen(row, col, board, rows, cols, lef_diag, right_diag)
            put_queen(row + 1, board, rows, cols, lef_diag, right_diag)
            remove_queen(row, col, board, rows, cols, lef_diag, right_diag)


n = 8
board = []
for row in range(n):
    board.append(list("-" * 8))

put_queen(0, board, set(), set(), set(), set())
