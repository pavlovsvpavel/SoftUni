number = float(input())
flag = False

if number == 0:
    print("zero")
    exit()
elif number < 0:
    flag = True
    number = abs(number)

if not flag:
    if number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if number < 1:
        print("small negative")
    elif number > 1000000:
        print("large negative")
    else:
        print("negative")
