text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

result = [x for x in text if x not in vowels]
print("".join(result))
