from collections import deque


def print_path(matrix):
    for i, current_row in enumerate(matrix):
        if i % 2 != 0:
            current_row = current_row[::-1]
        print("".join(current_row))


rows, cols = [int(x) for x in input().split(" ")]
snake = deque(input())

matrix = []

for row in range(rows):
    row_data = []
    for col in range(cols + 1):
        current_el = snake.popleft()
        row_data.append(current_el)
        snake.append(current_el)

        if len(row_data) == cols:
            matrix.append(row_data)
            break

print_path(matrix)
