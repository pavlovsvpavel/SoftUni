string = input()
result = []
for pos, char in enumerate(range(len(string) - 1), 1):
    if string[char] != string[pos]:
        result.append(string[char])

print(f'{"".join(result)}{string[-1]}')
