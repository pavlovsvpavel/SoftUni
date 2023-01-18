count_letters = int(input())

for i in range(ord("a"), (ord("a") + count_letters)):
    letter_1 = chr(i)
    for k in range(ord("a"), (ord("a") + count_letters)):
        letter_2 = chr(k)
        for j in range(ord("a"), (ord("a") + count_letters)):
            letter_3 = chr(j)
            print(f"{letter_1}{letter_2}{letter_3}")
