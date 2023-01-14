word = input()
result = []

for i in range(len(word)):
    for ch in word[i]:
        if ch.isupper():
            result.append(i)

print(result)
