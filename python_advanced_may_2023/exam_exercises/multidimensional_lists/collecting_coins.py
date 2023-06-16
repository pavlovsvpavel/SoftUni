from math import floor


def find_player_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "P":
                return i, j


def out_of_matrix(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


def new_position(row, col, size):
    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    elif col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    return row, col


size = int(input())
field = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

total_coins = 0
hit_wall = False
player_path = []

player_row, player_col = find_player_pos(field)
field[player_row][player_col] = 0
player_path.append(list((player_row, player_col)))

while total_coins < 100 and not hit_wall:
    direction = input()

    player_row, player_col = directions[direction](player_row, player_col)

    if out_of_matrix(player_row, player_col, size):
        player_row, player_col = new_position(player_row, player_col, size)

    player_path.append(list((player_row, player_col)))

    if field[player_row][player_col] == "X":
        total_coins /= 2
        hit_wall = True
        break
    else:
        total_coins += field[player_row][player_col]
        field[player_row][player_col] = 0

if hit_wall or total_coins < 100:
    print(f"Game over! You've collected {floor(total_coins)} coins.")
else:
    print(f"You won! You've collected {floor(total_coins)} coins.")

print("Your path:")
[print(x) for x in player_path]

