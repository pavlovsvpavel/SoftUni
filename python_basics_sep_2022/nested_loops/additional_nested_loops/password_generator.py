num1 = int(input())
num2 = int(input())
flag = False

for a in range(1, num1):
    for b in range(1, num1):
        for c in range(97, 97 + num2):
            c = chr(c)
            for d in range(97, 97 + num2):
                d = chr(d)
                for e in range(1, num1 + 1):
                    if e > a and e > b:
                        flag = True
                    if flag:
                        print(f"{a}{b}{c}{d}{e}", end=" ")
                        flag = False






