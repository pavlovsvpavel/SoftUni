def add_elements_to_set(args):
    result = set()
    for el in args:
        if el.isdigit():
            result.add(el)
    return result


def remove_elements_from_set(args, my_set):
    result = set(my_set)
    for el in args:
        if el.isdigit() and el in result:
            result.remove(el)
    return result


set_1 = {x for x in input().split(" ")}
set_2 = {x for x in input().split(" ")}
n = int(input())

for _ in range(n):
    command_args = input().split(" ")
    command = command_args[0]
    sub_command = command_args[1]

    if command == "Add" and sub_command == "First":
        set_1.update(add_elements_to_set(command_args))
    elif command == "Add" and sub_command == "Second":
        set_2.update(add_elements_to_set(command_args))
    elif command == "Remove" and sub_command == "First":
        set_1 = remove_elements_from_set(command_args, set_1)
    elif command == "Remove" and sub_command == "Second":
        set_2 = remove_elements_from_set(command_args, set_2)
    elif command == "Check":
        subset_1 = set_1.issubset(set_2)
        subset_2 = set_2.issubset(set_1)
        if subset_1 or subset_2:
            print("True")
        else:
            print("False")

print(", ".join(sorted(set_1, key=int)))
print(", ".join(sorted(set_2, key=int)))
