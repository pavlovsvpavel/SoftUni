def find_tunnel_pos(matrix):
    coords = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "T":
                coords.append((i, j))

    return coords


size = int(input())
car_number = input()

route = [input().split() for _ in range(size)]

directions = {
        "up": lambda x, y: (x - 1, y),
        "down": lambda x, y: (x + 1, y),
        "right": lambda x, y: (x, y + 1),
        "left": lambda x, y: (x, y - 1),
    }

car_row, car_col = 0, 0
distance_km = 0

tunnel_pos = find_tunnel_pos(route)

while True:
    command = input()

    if command == "End":
        print(f"Racing car {car_number} DNF.")
        break

    car_row, car_col = directions[command](car_row, car_col)

    if (car_row, car_col) in tunnel_pos:
        route[tunnel_pos[0][0]][tunnel_pos[0][1]] = "."
        tunnel_pos.remove((car_row, car_col))
        distance_km += 30
        car_row, car_col = tunnel_pos[0]
        route[tunnel_pos[0][0]][tunnel_pos[0][1]] = "."

    elif route[car_row][car_col] == "F":
        distance_km += 10
        print(f"Racing car {car_number} finished the stage!")
        break

    else:
        distance_km += 10

route[car_row][car_col] = "C"

print(f"Distance covered {distance_km} km.")

[print(*inner_list, sep="") for inner_list in route]

