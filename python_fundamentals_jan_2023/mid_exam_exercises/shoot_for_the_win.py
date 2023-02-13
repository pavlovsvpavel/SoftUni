def reduce_increase_func(index, lst):
    result = []
    for x in lst:
        if x == - 1:
            result.append(-1)
            continue
        if x > lst[index]:
            x -= lst[index]
            result.append(x)
        else:
            x += lst[index]
            result.append(x)
    return result


user_input = input()
targets_list = [int(x) for x in user_input.split(" ")]
shots_counter = 0
cleared_indexes = []

while True:
    target_index = input()
    if target_index == "End":
        break
    else:
        target_index = int(target_index)
    if target_index in cleared_indexes:
        continue

    if target_index < len(targets_list):
        shots_counter += 1
        cleared_indexes.append(target_index)
        targets_list = reduce_increase_func(target_index, targets_list)
        targets_list[target_index] = - 1
    else:
        continue

targets_result = [str(x) for x in targets_list]
print("Shot targets: " + str(shots_counter) + " -> " + " ".join(targets_result))

