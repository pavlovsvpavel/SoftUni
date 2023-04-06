def letters_symbols(lst):
    result = []
    for ch in string_to_list:
        if not ch.isalnum():
            result.append(ch)
        elif ch.isalpha():
            result.append(ch)
    return result


string = input()
string_to_list = [x for x in string]

nums_list = [int(num) for num in string_to_list if num.isdigit()]
non_num_list = letters_symbols(string_to_list)
take_indexes = [nums_list[x] for x in range(len(nums_list)) if x % 2 == 0]
skip_indexes = [nums_list[y] for y in range(len(nums_list)) if y % 2 != 0]
# take and skip indexes always will be even
length_indexes = len(take_indexes)
hidden_message = []

for pos, idx in enumerate(range(length_indexes)):
    take_idx = take_indexes[pos]
    skip_idx = skip_indexes[pos]
    hidden_message = hidden_message + non_num_list[:take_idx]
    non_num_list = non_num_list[take_idx + skip_idx:]

print("".join(hidden_message))
