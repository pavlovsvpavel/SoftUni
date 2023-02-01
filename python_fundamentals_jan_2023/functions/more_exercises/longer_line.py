import math


def sides_diagonals_calc(a, b, c, d):
    my_list = [a, b, c, d]
    coordinates_list = list(map(abs, my_list))
    side_a = coordinates_list[0] + coordinates_list[2]
    side_b = coordinates_list[1] + coordinates_list[3]
    diagonal = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
    return diagonal_results.append(diagonal)


def longest_line(a, b):
    if a > b:
        line_coordinates = [x1, y1, x2, y2]
    else:
        line_coordinates = [x3, y3, x4, y4]

    return line_coordinates


def rectangle_or_square(x, y):
    """
    :param x: x coordinate of point
    :param y: y coordinate of point
    :return: Checks and return the type of figure which the coordinates are forming
    """
    inputs_list = [x, y]
    coordinates_list = list(map(abs, inputs_list))
    if coordinates_list[0] == coordinates_list[1]:
        return "square"
    else:
        return "rectangle"


def diagonals_calculation(a, b):
    """
    :param a: x coordinate of point
    :param b: y coordinate of point
    :return: calculates the diagonal of the figure
    """
    if rectangle_or_square(new_x1, new_y1) == "rectangle" or rectangle_or_square(new_x2, new_y2) == "rectangle":
        diagonal = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return all_diagonals.append(diagonal)
    elif rectangle_or_square(new_x1, new_y1) == "square" or rectangle_or_square(new_x2, new_y2) == "square":
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
    result_1 = []
    for i in range(index * 2, (index * 2 + 1) + 1):
        result_1.append(math.floor(initial_list[i]))
    index -= 1
    for k in range(index * 2, (index * 2 + 1) + 1):
        result_1.append(math.floor(initial_list[k]))
    print(f"{result_1[0], result_1[1]}({result_1[2]}, {result_1[3]})")
    return


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())
diagonal_results = []
sides_diagonals_calc(x1, y1, x2, y2)
sides_diagonals_calc(x3, y3, x4, y4)
longest_line(diagonal_results[0], diagonal_results[1])

rectangle_or_square(longest_line(diagonal_results[0], diagonal_results[1])[0], longest_line(diagonal_results[0],
                                                                                            diagonal_results[1])[1])
new_x1 = longest_line(diagonal_results[0], diagonal_results[1])[0]
new_y1 = longest_line(diagonal_results[0], diagonal_results[1])[1]
new_x2 = longest_line(diagonal_results[0], diagonal_results[1])[2]
new_y2 = longest_line(diagonal_results[0], diagonal_results[1])[3]

all_diagonals = []
diagonals_calculation(new_x1, new_y1)
diagonals_calculation(new_x2, new_y2)
coordinates(new_x1, new_y1, new_x2, new_y2)

