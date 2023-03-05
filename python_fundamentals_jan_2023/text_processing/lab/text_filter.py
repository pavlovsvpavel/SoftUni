ban_words = input().split(", ")
text = input()

for word in ban_words:
    word_length = len(word)
    replace_with_asteriks = word_length * "*"
    while word in text:
        text = text.replace(word, replace_with_asteriks)

print(text)
