string = list(input())
explosion_left = 0

for pos, el in enumerate(string):
    if el == ">":
        current_explosion = int(string[pos + 1])
        if current_explosion > 0:
            for idx in range(current_explosion + explosion_left):
                if explosion_left > 0:
                    explosion_left = 0
                if pos == len(string) - 1:
                    break
                if string[pos + 1] != ">":
                    string.pop(pos + 1)
                else:
                    explosion_left = current_explosion - 1
                    break

print("".join(string))
