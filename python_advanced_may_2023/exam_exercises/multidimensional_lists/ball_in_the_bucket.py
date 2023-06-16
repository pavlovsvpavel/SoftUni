def coords_check(matrix, position):
    row, col = position

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
        return 0

    if matrix[row][col] == "B":
        matrix[row][col] = 0
        return sum_of_column_elements(matrix, col)
    else:
        return 0


def sum_of_column_elements(matrix, col):
    rows = len(matrix)
    result = []

    for i in range(rows):
        el = matrix[i][col]
        result.append(el)

    return sum(result)


SIZE = 6
TIMES = 3

board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(SIZE)]

total_points = 0

for _ in range(TIMES):
    coords = tuple(int(x) for x in input().strip("(").strip(")").split(", "))

    total_points += coords_check(board, coords)

if 100 <= total_points <= 199:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points <= 299:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
