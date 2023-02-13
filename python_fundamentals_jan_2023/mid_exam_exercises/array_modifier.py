def swap_func(lst):
    lst[index_1], lst[index_2] = lst[index_2], lst[index_1]
    return


def multiply_func(lst):
    result = lst[index_1] * lst[index_2]
    lst[index_1] = result
    return


def subtract_func(lst):
    result = list(map(lambda x: x - 1, lst))
    return result


user_input = input()
int_lst = [int(x) for x in user_input.split(" ")]

while True:
    command = input()
    command_lst = [x for x in command.split(" ")]
    single_command = command_lst[0]
    if single_command == "end":
        break

    if single_command == "swap":
        index_1 = int(command_lst[1])
        index_2 = int(command_lst[2])
        # int_lst[index_1], int_lst[index_2] = int_lst[index_2], int_lst[index_1]
        swap_func(int_lst)
    elif single_command == "multiply":
        index_1 = int(command_lst[1])
        index_2 = int(command_lst[2])
        # result = int_lst[index_1] * int_lst[index_2]
        # int_lst[int(command_lst[1])] = result
        multiply_func(int_lst)
    elif single_command == "decrease":
        # int_lst = list(map(lambda x: x - 1, int_lst))
        int_lst = subtract_func(int_lst)


final_result = [str(x) for x in int_lst]
print(", ".join(final_result))

