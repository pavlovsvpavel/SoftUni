def add_user(my_dict, user, side):
    for users in my_dict.values():
        if user in users:
            return
    my_dict[side] = my_dict.get(side, []) + [user]


def switch_user(my_dict, side, user):
    for sides, users in my_dict.items():
        if user in users:
            my_dict[sides].remove(user)
            break
    my_dict[side] = my_dict.get(side, []) + [user]
    print(f"{user} joins the {side} side!")


force_book = {}
while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        add_user(force_book, user, side)
    elif "->" in command:
        user, side = command.split(" -> ")
        switch_user(force_book, side, user)

for side, names in force_book.items():
    if names:
        print(f"Side: {side}, Members: {len(names)}")
        for user in names:
            print(f"! {user}")
