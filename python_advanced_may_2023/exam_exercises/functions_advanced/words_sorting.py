from collections import defaultdict


def words_sorting(*args, value=0):
    words_dict = defaultdict(int)
    sum_of_all_values = 0
    result = []

    def ascii_value():
        letters_sum = 0
        for letter in word:
            letters_sum += ord(letter)

        return letters_sum

    for word in args:
        words_dict[word] = ascii_value()

    for value in words_dict.values():
        sum_of_all_values += value

    if sum_of_all_values % 2 == 0:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))
    else:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: -x[1]))

    for single_word, word_value in sorted_dict.items():
        result.append(f"{single_word} - {word_value}")

    return "\n".join(result)


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
