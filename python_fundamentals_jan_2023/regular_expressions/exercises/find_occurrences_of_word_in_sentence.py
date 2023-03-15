import re

input_string = input()
searched_word = input()

regex = rf"\b({searched_word})+\b"  # rf means that the regular expression can receive a variable
result = re.findall(regex, input_string, re.IGNORECASE)

print(len(result))
