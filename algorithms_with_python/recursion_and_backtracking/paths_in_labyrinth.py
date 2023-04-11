def find_path(row, col, lab, direction, path):
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return

    if lab[row][col] in "*v":
        return

    path.append(direction)

    if lab[row][col] == "e":
        print("".join(path))
    else:
        lab[row][col] = "v"
        find_path(row + 1, col, lab, "D", path)
        find_path(row - 1, col, lab, "U", path)
        find_path(row, col + 1, lab, "R", path)
        find_path(row, col - 1, lab, "L", path)
        lab[row][col] = "-"

    path.pop()


rows = int(input())
cols = int(input())

labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

find_path(0, 0, labyrinth, "", [])
