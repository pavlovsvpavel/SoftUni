elements = input().split(" ")
dictionary = {}

for element in elements:
    element_lower = element.lower()
    # if element_lower not in dictionary.keys():
    #     dictionary[element_lower] = 0
    dictionary[element_lower] = dictionary.get(element_lower, 0) + 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")



