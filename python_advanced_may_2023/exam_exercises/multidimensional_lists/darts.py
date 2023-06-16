from collections import deque


def coords_check(matrix, position, max_points):
    row, col = position
    points = 0

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
        points = 0

    elif matrix[row][col] == "D":
        points = sum_of_points(matrix, row, col) * 2

    elif matrix[row][col] == "T":
        points = sum_of_points(matrix, row, col) * 3

    elif matrix[row][col] == "B":
        points = max_points

    else:
        points += matrix[row][col]

    return points


def sum_of_points(matrix, row, col):
    result = [
        matrix[0][col],
        matrix[len(matrix) - 1][col],
        matrix[row][0],
        matrix[row][len(matrix) - 1]
    ]

    return sum(result)


SIZE = 7
POINTS = 501

players_names = deque(input().split(", "))
board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

starting_points = {
    players_names[0]: [POINTS, 0],
    players_names[1]: [POINTS, 0],
}

while True:
    coords = tuple(int(x) for x in input().strip("(").strip(")").split(", "))

    current_player = players_names[0]
    players_names.rotate()

    current_points = coords_check(board, coords, POINTS)

    starting_points[current_player][0] -= current_points
    starting_points[current_player][1] += 1

    if starting_points[current_player][0] <= 0:
        print(f"{current_player} won the game with {starting_points[current_player][1]} throws!")
        break
