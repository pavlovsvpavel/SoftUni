user_input = input()
count_beggars = int(input())

my_list = user_input.split(", ")
list_beggars = [0] * count_beggars
count = 0

for i in range(len(my_list)):
    list_beggars[count] += int(my_list[i])
    count += 1

    if count >= count_beggars:
        count = 0

print(list_beggars)
