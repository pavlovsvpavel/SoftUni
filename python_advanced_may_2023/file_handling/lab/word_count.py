import re
words_dict = {}

pattern = r"[a-zA-Z]+"
with open("input.txt") as f:
    matches = re.findall(pattern, f.read().lower())

with open("words.txt") as f:
    words = f.read().lower()

    for word in words.split():
        counter = matches.count(word)
        words_dict[word] = counter

words_sorted = sorted(words_dict.items(), key=lambda x: -x[1])

with open("output.txt", "w") as f:
    for word, counts in words_sorted:
        f.write(f"{word} - {counts}\n")
