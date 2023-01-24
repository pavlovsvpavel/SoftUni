user_string = input()

my_list = user_string.split(" ")

for number in range(len(my_list)):
    my_list[number] = int(my_list[number]) * - 1

print(my_list)

