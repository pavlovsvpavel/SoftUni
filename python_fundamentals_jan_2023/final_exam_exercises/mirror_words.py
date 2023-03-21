import re

input_string = input()
regex = r"(#|@)(?P<word>[A-Za-z]{3,})\1{2}(?P<next_word>[A-Za-z]{3,})\1"
matches = [m.groupdict() for m in re.finditer(regex, input_string)]
mirror_words = {}
for idx in range(len(matches)):
    word_one = matches[idx]["word"]
    word_two = matches[idx]["next_word"]
    reversed_word = word_two[::-1]
    if word_one == reversed_word:
        mirror_words[word_one] = word_two

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
if mirror_words:
    print("The mirror words are:")
    print(", ".join(f"{key} <=> {value}" for key, value in mirror_words.items()))
else:
    print("No mirror words!")
