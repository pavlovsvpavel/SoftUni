def average_sum_of_integers(lst):
    result = sum(lst) / len(lst)
    return result


def top_numbers(lst):
    top_list = []
    for num in lst:
        if num > average_sum_of_integers(num_lst):
            top_list.append(num)
    return top_list


def top_5(lst):
    lst.sort(reverse=True)
    lst = lst[:5]
    return lst


def int_to_string_list(lst):
    if len(lst) == 0:
        return "No"
    else:
        lst = [str(x) for x in lst]
        return " ".join(lst)


user_input = input()
num_lst = [int(x) for x in user_input.split(" ")]

average_sum_of_integers(num_lst)
top_numbers(num_lst)
top_5(top_numbers(num_lst))
print(int_to_string_list(top_5(top_numbers(num_lst))))
