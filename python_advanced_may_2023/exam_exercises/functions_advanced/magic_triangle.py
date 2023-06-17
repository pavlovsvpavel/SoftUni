def get_magic_triangle(n):
    matrix = [[1], [1, 1]]

    for i in range(2, n):
        row_data = [1]
        counter = 0

        for j in range(1, i):
            row_data.append(matrix[i - 1][counter] + matrix[i - 1][counter + 1])
            counter += 1

        row_data.append(1)
        matrix.append(row_data)

    return matrix


get_magic_triangle(5)
