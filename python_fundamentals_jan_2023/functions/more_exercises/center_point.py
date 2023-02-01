import math


def rectangle_or_square(a, b):
    """
    :param a: x coordinate of point
    :param b: y coordinate of point
    :return: Checks and return the type of figure which the coordinates are forming
    """
    inputs_list = [abs(a), abs(b)]
    if inputs_list[0] == inputs_list[1]:
        return "square"
    else:
        return "rectangle"


def diagonals_calculation(a, b):
    """
    :param a: x coordinate of point
    :param b: y coordinate of point
    :return: calculates the diagonal of the figure
    """
    if rectangle_or_square(x1, y1) == "rectangle" or rectangle_or_square(x2, y2) == "rectangle":
        diagonal = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return all_diagonals.append(diagonal)
    elif rectangle_or_square(x1, y1) == "square" or rectangle_or_square(x2, y2) == "square":
        diagonal = a * math.sqrt(2)
        return all_diagonals.append(diagonal)


def coordinates(a, b, c, d):
    """
    :param a: x coordinate of first point
    :param b: y coordinate of first point
    :param c: x coordinate of second point
    :param d: y coordinate of second point
    :return: The smallest diagonal which means that the point is closer to the center of coordinate system.
    The result is printing the point coordinates
    """
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

