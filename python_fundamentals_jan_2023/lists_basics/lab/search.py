count_lines = int(input())
magic_word = input()

my_list = []

for _ in range(count_lines):
    user_input = input()
    my_list.append(user_input)

print(my_list)

for i in range(len(my_list) - 1, -1, -1):
    if magic_word not in my_list[i]:
        my_list.remove(my_list[i])

print(my_list)
