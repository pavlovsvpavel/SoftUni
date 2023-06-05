def check_field_and_obstacle(matrix, row, col, obstacles):
    if (row, col) in obstacles:
        return True

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[row]):
        return True


rows, cols = (int(x) for x in input().split())
playground = [input().split() for _ in range(rows)]

blind_man_pos = 0, 0
obstacles_pos = set()
players_pos = set()

directions = {
    "up": (-1, 0),
    "down": (+1, 0),
    "right": (0, +1),
    "left": (0, -1),
}

for i in range(rows):
    for j in range(cols):
        if playground[i][j] == "B":
            blind_man_pos = i, j

        elif playground[i][j] == "O":
            obstacle_pos = i, j
            obstacles_pos.add(obstacle_pos)

        elif playground[i][j] == "P":
            player_pos = i, j
            players_pos.add(player_pos)

touched_players = 0
moves = 0
while True:
    command = input()

    if command == "Finish" or touched_players == 3:
        break

    current_row, current_col = (
        blind_man_pos[0] + directions[command][0],
        blind_man_pos[1] + directions[command][1]
    )

    if check_field_and_obstacle(playground, current_row, current_col, obstacles_pos):
        continue

    if (current_row, current_col) in players_pos:
        touched_players += 1
        playground[current_row][current_col] = "-"

    moves += 1
    blind_man_pos = current_row, current_col

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")
