def find_santa_pos():
    for i in range(rows):
        for j in range(cols):
            if field[i][j] == "Y":
                return i, j


def count_of_all_items():
    decorations = 0
    gifts = 0
    cookies = 0
    for i in range(rows):
        for j in range(cols):
            if field[i][j] == "D":
                decorations += 1
            elif field[i][j] == "G":
                gifts += 1
            elif field[i][j] == "C":
                cookies += 1

    return decorations, gifts, cookies


def check_for_item(matrix, row, col):
    decoration = 0
    gift = 0
    cookie = 0

    if matrix[row][col] == "D":
        decoration += 1

    elif matrix[row][col] == "G":
        gift += 1

    elif matrix[row][col] == "C":
        cookie += 1

    return decoration, gift, cookie


def indices_check(row, col, n_rows, n_cols):
    if row < 0:
        row = n_rows - 1
    if col < 0:
        col = n_cols - 1
    if row == n_rows:
        row = 0
    if col == n_cols:
        col = 0

    return row, col


rows, cols = [int(x) for x in input().split(", ")]
field = [input().split() for _ in range(rows)]

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}

santa_pos = find_santa_pos()

all_items = sum(count_of_all_items())
flag = False
while True:

    if flag:
        break

    command = input()

    if command == "End":
        break

    direction, steps = [int(x) if x.isdigit() else x for x in command.split("-")]

    for step in range(steps):
        field[santa_pos[0]][santa_pos[1]] = "x"
        santa_pos = directions[direction](santa_pos[0], santa_pos[1])

        if santa_pos[0] < 0 or santa_pos[1] < 0 or \
                santa_pos[0] == rows or santa_pos[1] == cols:

            santa_pos = indices_check(santa_pos[0], santa_pos[1], rows, cols)

        curr_decorations, curr_gifts, curr_cookies = check_for_item(field, *santa_pos)

        items["Christmas decorations"] += curr_decorations
        items["Gifts"] += curr_gifts
        items["Cookies"] += curr_cookies

        field[santa_pos[0]][santa_pos[1]] = "Y"

        if all_items == sum(items.values()):
            print("Merry Christmas!")
            flag = True
            break

print("You've collected:")

for item, qty in items.items():
    print(f"- {qty} {item}")

[print(*inner_list) for inner_list in field]



