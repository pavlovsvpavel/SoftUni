my_list = [int(x) for x in input().split(" ")]


while True:
    command = input().split(" ")
    if "end" in command:
        break

    even_odd_list = []

    if command[0] == "exchange":
        idx_1 = int(command[1])

        if idx_1 > len(my_list) - 1 or idx_1 < 0:
            print("Invalid index")
            continue

        my_list = my_list[idx_1 + 1:] + my_list[:idx_1 + 1]

    if command[0] == "max" or command[0] == "min":
        idx_2 = command[1]
        if idx_2 == "odd":
            for i in my_list:
                if i % 2 != 0:
                    even_odd_list.append(i)
        elif idx_2 == "even":
            for i in my_list:
                if i % 2 == 0:
                    even_odd_list.append(i)

        if not even_odd_list:
            print("No matches")
            continue

        if command[0] == "max":
            max_num = max(*even_odd_list)
            print(my_list.index(max_num))
        else:
            min_num = min(*even_odd_list)
            print(my_list.index(min_num))

    if command[0] == "first" or command[0] == "last":
        numbers_count = int(command[1])
        idx_3 = command[2]
        if idx_3 == "odd":
            for i in my_list:
                if i % 2 != 0:
                    even_odd_list.append(i)
        elif idx_3 == "even":
            for i in my_list:
                if i % 2 == 0:
                    even_odd_list.append(i)

        if 0 <= len(even_odd_list) > numbers_count:
            if command[0] == "first":
                even_odd_list = even_odd_list[:numbers_count]
                print(even_odd_list)
            else:
                even_odd_list = even_odd_list[numbers_count:]
                print(even_odd_list)
        elif len(even_odd_list) < numbers_count:
            print(even_odd_list)
        else:
            print("Invalid count")

print(my_list)



