def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids = []
    naughty_kids = []
    result = []

    def move_kid(kid_info):
        if type_of_kid == "Nice":
            nice_kids.append(kid_info[1])

        else:
            naughty_kids.append(kid_info[1])

        santa_list.remove(kid_info)

    def check_counting_number():
        matches = []

        for command in santa_list:
            if command[0] == int(counting_number):
                matches.append(command)

        if len(matches) == 1:
            move_kid(matches[0])

    def check_name():
        matches = []

        for command in santa_list:
            if command[1] == kid_name:
                matches.append(command)

        if len(matches) == 1:
            move_kid(matches[0])

    for data in args:
        counting_number, type_of_kid = data.split("-")
        check_counting_number()

    for kid_name, type_of_kid in kwargs.items():
        check_name()

    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")
    if santa_list:
        result.append(f"Not found: {', '.join(name[1] for name in santa_list)}")

    return "\n".join(result)


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

