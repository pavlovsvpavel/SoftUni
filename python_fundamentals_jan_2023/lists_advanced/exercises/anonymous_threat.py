def merge(lst, s_idx, e_idx):
    result = []
    for i in range(s_idx, e_idx + 1):
        result.append(lst[i])
    return "".join(result)


def divide(lst, idx, parts):
    result = []
    current_word = "".join([lst[idx]])
    if parts == 0:
        result = current_word
        return result

    word_length = len(lst[idx])
    count_char = int(word_length // parts)  # How many letters in one element
    left_parts = int(word_length % parts)   # Remaining elements with left letters
    element_to_add = ""
    last_part = word_length - count_char - left_parts  # Last part starting index
    if left_parts == 0:
        for i in range(word_length):
            element_to_add += current_word[i]
            if len(element_to_add) == count_char:
                result.append(element_to_add)
                element_to_add = ""
            else:
                continue
    else:
        for k in range(word_length - 1 - left_parts):
            element_to_add += current_word[k]
            if len(element_to_add) == count_char:
                result.append(element_to_add)
                element_to_add = ""
            else:
                continue

        element_to_add = current_word[last_part:]
        result.append(element_to_add)
    return " ".join(result)


strings = input().split(" ")

while True:
    command = input().split(" ")
    current_command = command[0]
    if current_command == "3:1":
        break

    if current_command == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 > start_index or start_index >= len(strings):
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1
        strings = strings[:start_index] + [merge(strings, start_index, end_index)] + strings[end_index + 1:]

    elif current_command == "divide":
        index = int(command[1])
        partitions = int(command[2])
        strings = strings[:index] + [divide(strings, index, partitions)] + strings[index + 1:]

print(" ".join(strings))
