name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        exit()
    else:
        num_of_characters = len(name)

    if num_of_characters < 5:
        print(f"{name} goes to Gryffindor.")
    elif num_of_characters == 5:
        print(f"{name} goes to Slytherin.")
    elif num_of_characters == 6:
        print(f"{name} goes to Ravenclaw.")
    elif num_of_characters > 6:
        print(f"{name} goes to Hufflepuff.")

    name = input()

print("Welcome to Hogwarts.")
