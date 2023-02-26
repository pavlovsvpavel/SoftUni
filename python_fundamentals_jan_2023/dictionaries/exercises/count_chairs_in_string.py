string = input().split(" ")
dictionary = {}
for word in string:
    for char in word:
        if char not in dictionary.keys():
            dictionary[char] = 0
        dictionary[char] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")



