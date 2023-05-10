def read_matrix():
    current_matrix = []
    for _ in range(int(input())):
        row_data = list(map(int, input().split(" ")))
        current_matrix.append(row_data)

    return current_matrix


def primary_diagonal_sum(matrix):
    diagonal_sum = 0
    elements = []
    for i in range(len(matrix)):
        element = matrix[i][i]
        diagonal_sum += element
        if element < 0:
            elements.append("(" + str(element) + ")")
        else:
            elements.append(str(element))

    return elements, diagonal_sum


def secondary_diagonal_sum(matrix):
    diagonal_sum = 0
    elements = []
    for i in range(len(matrix)):
        element = matrix[i][len(matrix) - 1 - i]
        diagonal_sum += element
        if element < 0:
            elements.append("(" + str(element) + ")")
        else:
            elements.append(str(element))

    return elements, diagonal_sum


def difference_func(diagonal_1, diagonal_2):
    primary_diag = diagonal_1[1]
    secondary_diag = diagonal_2[1]
    result = abs(primary_diag - secondary_diag)

    return result


matrix = read_matrix()
print(difference_func(primary_diagonal_sum(matrix), secondary_diagonal_sum(matrix)))
