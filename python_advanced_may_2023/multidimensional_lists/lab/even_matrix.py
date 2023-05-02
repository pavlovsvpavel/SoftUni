num_of_rows = int(input())
matrix = []

for _ in range(num_of_rows):
    row = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(row)

print(matrix)
