characters = input().split(", ")

my_dictionary = {key: ord(key) for key in characters}

print(my_dictionary)
