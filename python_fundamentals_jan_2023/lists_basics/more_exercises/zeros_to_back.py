user_input = input().split(", ")

my_list = []
counter = 0
for element in user_input:
    element = int(element)
    if element > 0:
        my_list.append(element)

    elif element == 0:
        counter += 1

my_list = (my_list + [0] * counter)

print(my_list)
