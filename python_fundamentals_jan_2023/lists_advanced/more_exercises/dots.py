def path(row, col, board):
    if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
        return 0
    if board[row][col] != ".":
        return 0

    board[row][col] = "v"

    result = 1
    result += path(row + 1, col, board)
    result += path(row - 1, col, board)
    result += path(row, col + 1, board)
    result += path(row, col - 1, board)
    return result


n = int(input())

board = []
dots_list = []
for _ in range(n):
    board.append(list(input().split(" ")))

for row in range(0, len(board[0]) - 1):
    for col in range(0, n - 1):
        dots = path(row, col, board)
        if dots == 0:
            continue
        dots_list.append(dots)

if dots_list:
    print(max(dots_list))
else:
    print("0")
