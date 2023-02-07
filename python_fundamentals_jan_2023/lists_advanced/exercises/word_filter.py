text = input()
words_list = text.split(" ")

even_length_word = list(filter(lambda word: len(word) % 2 == 0, words_list))

print("\n".join(even_length_word))
