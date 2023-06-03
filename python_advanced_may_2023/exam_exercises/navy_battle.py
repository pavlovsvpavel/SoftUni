def movements(matrix, row, col):
    ships_ = 0
    mines_ = 0
    if matrix[row][col] == "C":
        ships_ += 1
    elif matrix[row][col] == "*":
        mines_ += 1

    return ships_, mines_


def find_submarine_pos(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "S":
                return i, j


SIZE = int(input())
battlefield = [list(input()) for _ in range(SIZE)]

destroyed_ships = 0
hit_mines = 0

directions = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "right": lambda x, y: (x, y + 1),
        "left": lambda x, y: (x, y - 1),
    }

submarine_row, submarine_col = find_submarine_pos(battlefield, SIZE)
battlefield[submarine_row][submarine_col] = "-"

while True:
    command = input()

    if hit_mines == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_row}, {submarine_col}]!")
        break

    if destroyed_ships == 3:
        print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    current_row, current_col = directions[command](submarine_row, submarine_col)

    ships, mines = movements(battlefield, current_row, current_col)
    battlefield[current_row][current_col] = "-"

    destroyed_ships += ships
    hit_mines += mines

    submarine_row, submarine_col = current_row, current_col

battlefield[submarine_row][submarine_col] = "S"

[print(*inner_list, sep="") for inner_list in battlefield]
