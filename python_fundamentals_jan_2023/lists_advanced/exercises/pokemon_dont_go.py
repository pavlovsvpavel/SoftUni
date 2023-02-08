def changing_values(lst, idx):
    result = []
    removed_value = 0
    if idx < 0:
        removed_value = lst[0]
        lst[0] = lst[-1]
    elif idx > len(lst) - 1:
        removed_value = lst[-1]
        lst[-1] = lst[0]
    else:
        removed_value = lst.pop(idx)
    for num in lst:
        if num <= removed_value:
            num += removed_value
            result.append(num)
        elif num > removed_value:
            num -= removed_value
            result.append(num)
    return result, removed_value


numbers = input().split(" ")
num_list = list(map(int, numbers))
sum_of_el = 0
while True:
    if not num_list:
        break

    index = int(input())
    num_list, rem_value = changing_values(num_list, index)
    sum_of_el += rem_value

print(sum_of_el)
