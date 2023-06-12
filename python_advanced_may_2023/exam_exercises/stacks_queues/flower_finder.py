from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers_dict = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}

word_found = False

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for flower in flowers_dict.keys():
        flowers_dict[flower] = flowers_dict[flower].replace(current_vowel, "")
        flowers_dict[flower] = flowers_dict[flower].replace(current_consonant, "")

        if flowers_dict[flower] == "":
            print(f"Word found: {flower}")
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")


