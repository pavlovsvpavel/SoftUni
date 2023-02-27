def add_user(user, side):
    for users in force_book.values():
        if user in users:
            return
    force_book[side] = force_book.get(side, []) + [user]


def switch_user(side, user):
    for sides, users in force_book.items():
        if user in users:
            force_book[sides].remove(user)
            break
    force_book[side] = force_book.get(side, []) + [user]
    print(f"{user} joins the {side} side!")


force_book = {}
while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        add_user(user, side)
    elif "->" in command:
        user, side = command.split(" -> ")
        switch_user(side, user)

for side, names in force_book.items():
    if names:
        print(f"Side: {side}, Members: {len(names)}")
        for user in names:
            print(f"! {user}")
