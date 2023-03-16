import re
number_of_plants = int(input())

plants_collection = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    plants_collection[plant] = {'rarity': rarity, 'rating': []}

while True:
    command = input()

    if command == "Exhibition":
        break

    command_args = re.findall(r"[A-za-z0-9]+", command)
    plant = command_args[1]
    if plant not in plants_collection.keys():
        print("error")
        continue

    if command_args[0] == "Rate":
        rating = int(command_args[2])
        plants_collection[plant]["rating"].append(rating)
    elif command_args[0] == "Update":
        new_rarity = int(command_args[2])
        plants_collection[plant]["rarity"] = new_rarity
    elif command_args[0] == "Reset":
        plants_collection[plant]["rating"].clear()

print("Plants for the exhibition:")

for plant_name, values in plants_collection.items():
    final_rarity = values["rarity"]
    ratings = values["rating"]
    if len(ratings) > 0:
        avg_rating = sum(ratings) / len(ratings)
    else:
        avg_rating = 0
    print(f"- {plant_name}; Rarity: {final_rarity}; Rating: {avg_rating:.2f}")
