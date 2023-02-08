def check_word(word, lst):
    for i in range(len(lst)):
        if word in lst[i]:
            return word


string_1 = input().split(", ")
string_2 = input().split(", ")

# result = list(filter(lambda x: check_word(x, string_2), string_1))
result = [check_word(x, string_2) for x in string_1 if check_word(x, string_2) is not None]
print(result)
