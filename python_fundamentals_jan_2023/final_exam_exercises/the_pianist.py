number_of_pieces = int(input())

collection = {}
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = [composer, key]

while True:
    command = input()

    if command == "Stop":
        break

    command_args = command.split("|")

    if command_args[0] == "Add":
        new_piece = command_args[1]
        new_composer = command_args[2]
        new_key = command_args[3]
        if new_piece not in collection.keys():
            collection[new_piece] = [new_composer, new_key]
            print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
        else:
            print(f"{new_piece} is already in the collection!")
    elif command_args[0] == "Remove":
        piece = command_args[1]
        if piece in collection.keys():
            collection.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command_args[0] == "ChangeKey":
        piece = command_args[1]
        new_key = command_args[2]
        if piece in collection.keys():
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in collection.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")

