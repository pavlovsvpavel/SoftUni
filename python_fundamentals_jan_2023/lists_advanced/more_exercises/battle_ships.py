n = int(input())

matrix = []
destroyed_ships = 0
for _ in range(n):
    matrix.append(list([int(x) for x in input().split(" ")]))

attacks = input().split(" ")

for attack in attacks:
    row = int(attack[0])
    col = int(attack[2])
    current_ship_health = matrix[row][col]
    if current_ship_health > 0:
        matrix[row][col] -= 1
        if matrix[row][col] <= 0:
            destroyed_ships += 1

print(destroyed_ships)
