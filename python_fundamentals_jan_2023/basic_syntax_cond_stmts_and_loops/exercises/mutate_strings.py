word_1 = input()
word_2 = input()
unique_word = ""
prev_word = ""

for i in range(len(word_1)):
    unique_word += word_2[:i + 1] + word_1[i + 1:]
    if unique_word != word_1 and unique_word != prev_word:
        print(unique_word)
        prev_word = unique_word
        unique_word = ""
    else:
        unique_word = ""
        continue
