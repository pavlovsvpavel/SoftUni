def fill_the_box(*args):
    height, length, width = args[0], args[1], args[2]
    box_size = height * length * width
    all_cubes = 0

    def availability_check():
        return box_size >= all_cubes

    for el in (args[3:]):
        if el != "Finish":
            all_cubes += el
        else:
            break

    if availability_check():
        return f"There is free space in the box. You could put {box_size - all_cubes} more cubes."
    else:
        return f"No more free space! You have {all_cubes - box_size} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
