from collections import deque


def print_path(matrix):
    for i, row in enumerate(matrix):
        if i % 2 != 0:
            row = row[::-1]
        print("".join(map(str, row)))


rows, cols = [int(x) for x in input().split(" ")]
snake = input()

matrix = []
snake_copy = deque(snake)

for row in range(rows):
    row_data = []
    for col in range(cols + 1):
        current_el = snake_copy.popleft()
        row_data.append(current_el)
        snake_copy.append(current_el)

        if len(row_data) == cols:
            matrix.append(row_data)
            break

print_path(matrix)
