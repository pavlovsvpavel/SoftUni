from collections import deque


def out_of_matrix(row, col, size):
    return row < 0 or row >= size or col < 0 or col >= size


def new_position(row, col, size):
    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    elif col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    return row, col


def find_deposits_and_rocks(matrix, size):
    water_dep = []
    metal_dep = []
    concrete_dep = []
    rock = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "W":
                water_dep.append((i, j))
            elif matrix[i][j] == "M":
                metal_dep.append((i, j))
            elif matrix[i][j] == "C":
                concrete_dep.append((i, j))
            elif matrix[i][j] == "R":
                rock.append((i, j))

    return water_dep, metal_dep, concrete_dep, rock


def find_rover_pos(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == "E":
                return i, j


SIZE = 6
matrix = [input().split() for _ in range(SIZE)]
commands = deque(input().split(", "))

directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "right": lambda x, y: (x, y + 1),
    "left": lambda x, y: (x, y - 1),
}

water = 0
metal = 0
concrete = 0

rover_row, rover_col = find_rover_pos(matrix, SIZE)

while commands:
    current_command = commands.popleft()

    current_row, current_col = directions[current_command](rover_row, rover_col)

    change_pos = out_of_matrix(current_row, current_col, SIZE)

    if change_pos:
        current_row, current_col = new_position(current_row, current_col, SIZE)

    water_deposits, metal_deposits, concrete_deposits, rocks = find_deposits_and_rocks(matrix, SIZE)

    if (current_row, current_col) in rocks:
        print(f"Rover got broken at ({current_row}, {current_col})")
        break

    elif (current_row, current_col) in water_deposits:
        print(f"Water deposit found at ({current_row}, {current_col})")
        water += 1

    elif (current_row, current_col) in metal_deposits:
        print(f"Metal deposit found at ({current_row}, {current_col})")
        metal += 1

    elif (current_row, current_col) in concrete_deposits:
        print(f"Concrete deposit found at ({current_row}, {current_col})")
        concrete += 1

    rover_row, rover_col = current_row, current_col

if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
