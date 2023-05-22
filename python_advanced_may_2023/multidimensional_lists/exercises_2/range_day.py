from collections import deque


def indices_check(row_idx, col_idx, size):
    return 0 <= row_idx < size and 0 <= col_idx < size


def find_player_pos_and_targets_pos(matrix, size):
    targets = []
    player_position = ()
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "A":
                player_position = row, col
            if matrix[row][col] == "x":
                target_pos = row, col
                targets.append(target_pos)

    return player_position, len(targets)


SIZE = 5
matrix = [input().split() for _ in range(SIZE)]
n = int(input())
hit_targets = 0
hit_targets_coords = []
player_pos, all_targets = find_player_pos_and_targets_pos(matrix, SIZE)
directions = {
    "up": lambda x, y, z: (x - 1 - z, y),
    "down": lambda x, y, z: (x + 1 + z, y),
    "left": lambda x, y, z: (x, y - 1 - z),
    "right": lambda x, y, z: (x, y + 1 + z),
}

for _ in range(n):
    data = deque(input().split())
    command, curr_direction, steps = (
        data.popleft(),
        data.popleft(),
        int(data.popleft()) if data else 0
    )

    if command == "move":
        curr_row, curr_col = directions[curr_direction](player_pos[0], player_pos[1], steps - 1)

        if not indices_check(curr_row, curr_col, SIZE) or matrix[curr_row][curr_col] != ".":
            continue

        if matrix[curr_row][curr_col] == ".":
            player_pos = curr_row, curr_col

    elif command == "shoot":
        shoot_row, shoot_col = directions[curr_direction](player_pos[0], player_pos[1], steps)

        while True:
            if not indices_check(shoot_row, shoot_col, SIZE):
                break

            if matrix[shoot_row][shoot_col] == "x":
                hit_targets += 1
                hit_targets_coords.append([shoot_row, shoot_col])
                matrix[shoot_row][shoot_col] = "."
                break

            shoot_row, shoot_col = directions[curr_direction](shoot_row, shoot_col, steps)

    if hit_targets == all_targets:
        print(f"Training completed! All {hit_targets} targets hit.")
        break
else:
    print(f"Training not completed! {all_targets - hit_targets} targets left.")

[print(target) for target in hit_targets_coords]
