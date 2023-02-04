def shoot_func(lst, idx, pwr):
    if idx < len(lst):
        lst[idx] -= pwr
        if lst[idx] <= 0:
            lst.pop(idx)
        return


def add_values_func(lst, idx, val):
    result = lst[:idx] + [val] + lst[idx:]
    return result


def strike_func(lst, idx, rad):
    lst.pop(idx)
    result = lst[:idx - rad] + lst[idx + rad:]
    return result


user_input = input()
targets_list = [int(x) for x in user_input.split(" ")]
errors = []
while True:
    command = input()
    command_list = [x for x in command.split(" ")]
    single_command = command_list[0]
    if single_command == "End":
        break

    if single_command == "Shoot":
        index_1 = int(command_list[1])
        power = int(command_list[2])
        shoot_func(targets_list, index_1, power)
    elif single_command == "Add":
        index_2 = int(command_list[1])
        value = int(command_list[2])
        if index_2 < len(targets_list):
            targets_list = add_values_func(targets_list, index_2, value)
        else:
            errors.append("Invalid placement!")
    elif single_command == "Strike":
        index_3 = int(command_list[1])
        radius = int(command_list[2])
        if 0 < (index_3 - radius) < len(targets_list):
            targets_list = strike_func(targets_list, index_3, radius)
        else:
            errors.append("Strike missed!")

final_result = [str(x) for x in targets_list]
print("\n".join(errors))
print("|".join(final_result))
