from sys import maxsize
my_list = [int(x) for x in input().split(" ")]

while True:
    command = input().split(" ")

    if command[0] == "end":
        break

    if command[0] == "exchange":
        idx_1 = int(command[1])

        if idx_1 >= len(my_list) or idx_1 < 0:
            print("Invalid index")
        else:
            my_list = my_list[idx_1 + 1:] + my_list[:idx_1 + 1]

    elif command[0] == "max":
        idx_2 = command[1]
        index = None
        number = - maxsize
        if idx_2 == "odd":
            for i in range(len(my_list)):
                if my_list[i] % 2 != 0 and my_list[i] >= number:
                    index = i
                    number = my_list[i]
        elif idx_2 == "even":
            for i in range(len(my_list)):
                if my_list[i] % 2 == 0 and my_list[i] >= number:
                    index = i
                    number = my_list[i]

        if index or index == 0:
            print(index)
        else:
            print("No matches")

    elif command[0] == "min":
        idx_2 = command[1]
        index = None
        number = maxsize
        if idx_2 == "odd":
            for i in range(len(my_list)):
                if my_list[i] % 2 != 0 and my_list[i] <= number:
                    index = i
                    number = my_list[i]
        elif idx_2 == "even":
            for i in range(len(my_list)):
                if my_list[i] % 2 == 0 and my_list[i] <= number:
                    index = i
                    number = my_list[i]

        if index or index == 0:
            print(index)
        else:
            print("No matches")

    elif command[0] == "first":
        numbers_count = int(command[1])
        idx_3 = command[2]
        even_odd_list = []
        if numbers_count > len(my_list):
            print("Invalid count")
            continue

        if idx_3 == "odd":
            for i in my_list:
                if i % 2 != 0:
                    even_odd_list.append(i)
                if len(even_odd_list) == numbers_count:
                    break

        elif idx_3 == "even":
            for i in my_list:
                if i % 2 == 0:
                    even_odd_list.append(i)
                if len(even_odd_list) == numbers_count:
                    break

        if even_odd_list:
            print(even_odd_list)
        else:
            print("[]")

    elif command[0] == "last":
        numbers_count = int(command[1])
        idx_3 = command[2]
        even_odd_list = []
        if numbers_count > len(my_list):
            print("Invalid count")
            continue

        if idx_3 == "odd":
            for i in my_list:
                if i % 2 != 0:
                    even_odd_list.append(i)
                if len(even_odd_list) == numbers_count:
                    break

        elif idx_3 == "even":
            for i in my_list:
                if i % 2 == 0:
                    even_odd_list.append(i)
                if len(even_odd_list) == numbers_count:
                    break

        if even_odd_list:
            print(even_odd_list[-numbers_count:])
        else:
            print("[]")

print(my_list)
