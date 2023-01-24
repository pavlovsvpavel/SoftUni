my_list = []

for i in range(3):
    user_input = input()
    my_list.append(user_input)

my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)
