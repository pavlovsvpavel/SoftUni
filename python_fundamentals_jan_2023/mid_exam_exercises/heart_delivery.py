houses = [int(x) for x in input().split("@")]
mission_result = [0] * len(houses)
command_args = input()
command = command_args.split(" ")
last_house_index = 0
while command[0] != "Love!":
    house_index = int(command[1]) + last_house_index
    if house_index > len(houses) - 1:
        house_index = 0
    houses[house_index] -= 2
    last_house_index = house_index
    if houses[house_index] == 0:
        mission_result[house_index] = 1
        print(f"Place {house_index} has Valentine's day.")
    elif houses[house_index] < 0:
        print(f"Place {house_index} already had Valentine's day.")
    command_args = input()
    command = command_args.split(" ")

print(f"Cupid's last position was {last_house_index}.")

if mission_result.count(1) == len(houses):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {mission_result.count(0)} places.")
