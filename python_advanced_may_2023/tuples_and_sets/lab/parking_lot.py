n = int(input())

COMMAND_IN = "IN"
COMMAND_OUT = "OUT"
parking_lot = set()
for _ in range(n):
    command, plate_number = input().split(", ")

    if command == COMMAND_IN:
        parking_lot.add(plate_number)

    elif command == COMMAND_OUT:
        parking_lot.remove(plate_number)

if parking_lot:
    for plate in parking_lot:
        print(plate)
else:
    print("Parking Lot is Empty")
