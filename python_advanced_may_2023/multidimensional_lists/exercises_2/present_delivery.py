def indices_check(row_idx, col_idx, size):
    return 0 <= row_idx < size and 0 <= col_idx < size


def find_santa_pos_and_count_nice_kids(matrix, size):
    nice_kids = 0
    santa_pos = ()
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "S":
                santa_pos = row, col
            if matrix[row][col] == "V":
                nice_kids += 1

    return santa_pos, nice_kids


def house_visit(matrix, row, col):
        matrix[row][col] = "-"
        return 1


count_presents = int(input())
size_of_matrix = int(input())
matrix = [input().split() for _ in range(size_of_matrix)]

given_gifts_to_nice_kids = 0
santa_position, left_nice_kids = find_santa_pos_and_count_nice_kids(matrix, size_of_matrix)
matrix[santa_position[0]][santa_position[1]] = "-"
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}

while True:
    if count_presents == 0:
        break

    direction = input()

    if direction == "Christmas morning":
        break

    curr_row, curr_col = santa_position[0] + directions[direction][0], santa_position[1] + directions[direction][1]

    if not indices_check(curr_row, curr_col, size_of_matrix):
        continue

    if matrix[curr_row][curr_col] == "C":
        for move in directions:
            happy_row, happy_col = curr_row + directions[move][0], curr_col + directions[move][1]

            if matrix[happy_row][happy_col] == "V":
                given_gifts_to_nice_kids += house_visit(matrix, happy_row, happy_col)
                count_presents -= house_visit(matrix, happy_row, happy_col)
                left_nice_kids -= house_visit(matrix, happy_row, happy_col)

            elif matrix[happy_row][happy_col] == "X":
                count_presents -= house_visit(matrix, happy_row, happy_col)

            if count_presents == 0:
                break

    elif matrix[curr_row][curr_col] == "V":
        given_gifts_to_nice_kids += house_visit(matrix, curr_row, curr_col)
        count_presents -= house_visit(matrix, curr_row, curr_col)
        left_nice_kids -= house_visit(matrix, curr_row, curr_col)

    elif matrix[curr_row][curr_col] == "X":
        house_visit(matrix, curr_row, curr_col)

    santa_position = curr_row, curr_col

if count_presents == 0 and left_nice_kids > 0:
    print("Santa ran out of presents!")

matrix[santa_position[0]][santa_position[1]] = "S"

[print(*inner_list, sep=" ") for inner_list in matrix]

if left_nice_kids == 0:
    print(f"Good job, Santa! {given_gifts_to_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {left_nice_kids} nice kid/s.")
