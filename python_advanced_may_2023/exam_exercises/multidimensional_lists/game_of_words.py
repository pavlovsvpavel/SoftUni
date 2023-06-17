def find_player_pos(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "P":
                return i, j


def out_of_field(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


string = input()
size = int(input())
field = [list(input()) for _ in range(size)]

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

player_row, player_col = find_player_pos(field, size)
field[player_row][player_col] = "-"

moves = int(input())
for _ in range(moves):

    direction = input()

    row, col = directions[direction](player_row, player_col)

    if out_of_field(row, col, size):
        if string:
            string = string[:-1]
        continue

    if field[row][col] != "-":
        string += field[row][col]
        field[row][col] = "-"

    player_row, player_col = row, col

field[player_row][player_col] = "P"

print(string)

[print(*inner_list, sep="") for inner_list in field]
