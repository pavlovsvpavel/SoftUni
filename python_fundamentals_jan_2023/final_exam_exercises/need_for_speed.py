cars = int(input())
cars_collection = {}
MAX_FUEL = 75
MIN_MILEAGE = 10000
for _ in range(cars):
    car, mileage, fuel = input().split("|")
    if car not in cars_collection:
        cars_collection[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == "Stop":
        break

    command_args = command.split(" : ")

    if command_args[0] == "Drive":
        car_name = command_args[1]
        distance = int(command_args[2])
        needed_fuel = int(command_args[3])
        available_fuel = cars_collection[car_name][1]
        if available_fuel >= needed_fuel:
            cars_collection[car_name][1] -= needed_fuel
            cars_collection[car_name][0] += distance
            print(f"{car_name} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if cars_collection[car_name][0] > 100000:
                print(f"Time to sell the {car_name}!")
                cars_collection.pop(car_name)
        else:
            print("Not enough fuel to make that ride")
    elif command_args[0] == "Refuel":
        car_name = command_args[1]
        refill_qty = int(command_args[2])
        cars_collection[car_name][1] += refill_qty
        current_fuel = cars_collection[car_name][1]
        if current_fuel > MAX_FUEL:
            refill_qty = abs(current_fuel - refill_qty - MAX_FUEL)
            cars_collection[car_name][1] = MAX_FUEL

        print(f"{car_name} refueled with {refill_qty} liters")
    elif command_args[0] == "Revert":
        car_name = command_args[1]
        mileage_decrease = int(command_args[2])
        cars_collection[car_name][0] -= mileage_decrease
        current_mileage = cars_collection[car_name][0]
        if current_mileage >= MIN_MILEAGE:
            print(f"{car_name} mileage decreased by {mileage_decrease} kilometers")
        else:
            cars_collection[car_name][0] = MIN_MILEAGE

for car, values in cars_collection.items():
    print(f"{car} -> Mileage: {values[0]} kms, Fuel in the tank: {values[1]} lt.")
