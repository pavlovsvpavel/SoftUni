def palindrome_check(word):
    if word == word[::-1]:
        return word


words = input()
words_list = words.split(" ")
palindrome_word = input()

palindromes_list = [x for x in words_list if palindrome_check]
counter = palindromes_list.count(palindrome_word)

print(palindromes_list)
print(f"Found palindrome {counter} times")
