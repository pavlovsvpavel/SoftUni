number = input()
result = []

for i in range(len(number)):
    for ch in number[i]:
        result += ch

result.sort(reverse=True)

print("".join(result))

