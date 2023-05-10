def primary_diagonal_sum(matrix):
    result = 0
    elements = []
    for i in range(len(matrix)):
        element = matrix[i][i]
        result += element
        elements.append(element)
    return elements, result


def secondary_diagonal_sum(matrix):
    result = 0
    elements = []
    for i in range(len(matrix)):
        element = matrix[i][(len(matrix) - 1) - i]
        result += element
        elements.append(element)

    return elements, result


def print_func(result):
    return f"{', '.join(map(str, result[0]))}. Sum: {result[1]}"


num_of_rows = int(input())
matrix = [[int(el) for el in input().split(", ")] for row in range(num_of_rows)]

print(f"Primary diagonal: {print_func(primary_diagonal_sum(matrix))}")
print(f"Secondary diagonal: {print_func(secondary_diagonal_sum(matrix))}")
