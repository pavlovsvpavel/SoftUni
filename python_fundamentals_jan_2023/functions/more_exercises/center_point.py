import math


def rectangle_or_square(a, b):
    inputs_list = [abs(a), abs(b)]
    coordinates_list = list(map(abs, inputs_list))
    if coordinates_list[0] == coordinates_list[1]:
        return "square"
    else:
        return "rectangle"


def diagonals_calculation(a, b):
    if rectangle_or_square(x1, y1) == "rectangle" or rectangle_or_square(x2, y2) == "rectangle":
        diagonal = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return all_diagonals.append(diagonal)
    elif rectangle_or_square(x1, y1) == "square" or rectangle_or_square(x2, y2) == "square":
        diagonal = a * math.sqrt(2)
        return all_diagonals.append(diagonal)


def coordinates(a, b, c, d):
    initial_list = [a, b, c, d]
    diagonal = min(all_diagonals)
    index = all_diagonals.index(diagonal)
    result = []
    for i in range(index * 2, (index * 2 + 1) + 1):
        result.append(math.floor(initial_list[i]))
    return tuple(result)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
all_diagonals = []
diagonals_calculation(x1, y1)
diagonals_calculation(x2, y2)
print(coordinates(x1, y1, x2, y2))

