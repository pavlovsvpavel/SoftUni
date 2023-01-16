string = input().lower()

list_words = ["sand", "water", "fish", "sun"]
counter = 0

for word in list_words:
    if word in string:
        word_count = string.count(word)
        counter += word_count

print(counter)


