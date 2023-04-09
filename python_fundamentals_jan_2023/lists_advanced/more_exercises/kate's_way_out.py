def find_starting_point():
    for pos_row, row in enumerate(maze):
        for pos_col, col in enumerate(row):
            if col == "k":
                return pos_row, pos_col


def movements(row, col, maze):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]):
        return

    if maze[row][col] in "#v":
        return

    steps.append(1)

    if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]):  # find exit
        max_steps.append(sum(steps))

    maze[row][col] = "v"
    movements(row, col + 1, maze)  # right
    movements(row, col - 1, maze)  # left
    movements(row + 1, col, maze)  # down
    movements(row - 1, col, maze)  # up

    maze[row][col] = " "

    steps.pop()


rows = int(input())

maze = []
steps = []
max_steps = []
for row_1 in range(rows):
    maze.append(list(input()))

start_row, start_col = find_starting_point()
movements(start_row, start_col, maze)

if max_steps:
    print(f"Kate got out in {max(max_steps)} moves")
else:
    print(f"Kate cannot get out")
