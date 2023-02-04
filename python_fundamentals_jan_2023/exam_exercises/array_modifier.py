user_input = input()
int_lst = [int(x) for x in user_input.split(" ")]
command = input()
command_lst = [x for x in command.split(" ")]

while command_lst[0] != "end":
    if "swap" in command_lst:
        int_lst[int(command_lst[1])], int_lst[int(command_lst[2])] = int_lst[int(command_lst[2])], int_lst[
            int(command_lst[1])]
    elif "multiply" in command_lst:
        result = int_lst[int(command_lst[1])] * int_lst[int(command_lst[2])]
        int_lst[int(command_lst[1])] = result
    elif "decrease" in command_lst:
        int_lst = list(map(lambda x: x - 1, int_lst))

    command = input()
    command_lst = [x for x in command.split(" ")]

result = [str(x) for x in int_lst]
print(", ".join(result))
