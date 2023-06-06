from collections import deque


def find_exit_traps_walls(matrix):
    exit_position = []
    traps_pos = []
    walls_pos = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "E":
                exit_position.append((i, j))
            elif matrix[i][j] == "T":
                traps_pos.append((i, j))
            elif matrix[i][j] == "W":
                walls_pos.append((i, j))

    return exit_position, traps_pos, walls_pos


MAZE_SIZE = 6
players = deque(input().split(", "))
maze = [input().split() for _ in range(MAZE_SIZE)]

hit_walls = {
    players[0]: False,
    players[1]: False,
}

while True:
    current_player = players[0]
    players.rotate()

    coords = tuple([int(x) for x in input().strip("(").strip(")").split(", ")])

    if not hit_walls[current_player]:

        exit_pos, traps, walls = find_exit_traps_walls(maze)

        if coords in exit_pos:
            print(f"{current_player} found the Exit and wins the game!")
            break

        elif coords in traps:
            print(f"{current_player} is out of the game! The winner is {players[0]}.")
            break

        elif coords in walls:
            print(f"{current_player} hits a wall and needs to rest.")
            hit_walls[current_player] = True

    else:
        hit_walls[current_player] = False
