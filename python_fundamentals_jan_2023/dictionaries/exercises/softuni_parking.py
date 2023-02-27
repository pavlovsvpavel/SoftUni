n = int(input())
parking_lot = {}
for _ in range(n):
    command_args = input().split(" ")
    command = command_args[0]
    user_name = command_args[1]

    if command == "register":
        plate_number = command_args[2]
        if user_name not in parking_lot.keys():
            parking_lot[user_name] = plate_number
            print(f"{user_name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif command == "unregister":
        if user_name not in parking_lot.keys():
            print(f"ERROR: user {user_name} not found")
        else:
            parking_lot.pop(user_name)
            print(f"{user_name} unregistered successfully")

for user, license_number in parking_lot.items():
    print(f"{user} => {license_number}")
