number = int(input())

counter = 1
flag = False

for i in range(1, number + 1):
    for j in range(1, i + 1):

        if counter > number:
            flag = True
            break
        print(f"{counter} ", end="")
        counter += 1

    if flag:
        break
    print()
