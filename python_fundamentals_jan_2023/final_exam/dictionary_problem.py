input_line = input()
my_dictionary = {}
while ":" in input_line:
    collections = input_line.split(" | ")
    for el in collections:
        current_collection = el.split(": ")
        word = current_collection[0]
        definition = current_collection[1]
        if word not in my_dictionary.keys():
            my_dictionary[word] = []
        my_dictionary[word].append(definition)

    input_line = input()

words_list = input_line.split(" | ")

command = input()

if command == "Test":
    for check_word in words_list:
        if check_word in my_dictionary.keys():
            print(f"{check_word}:")
            for values in my_dictionary[check_word]:
                print(f" -{values}")

elif command == "Hand Over":
    for key in my_dictionary.keys():
        print(f"{key}", end=" ")
