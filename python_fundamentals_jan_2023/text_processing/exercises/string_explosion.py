string = list(input())
explosion_left = 0
counter = string.count(">")

for pos, el in enumerate(string, 1):
    if el == ">":
        counter -= 1
        current_explosion = int(string[pos])
        string.pop(pos)
        explosion_left += current_explosion - 1
        if explosion_left > 0 and string[pos] != ">":
            for _ in range(explosion_left):
                string.pop(pos)
                explosion_left = 0
    if counter == 0:
        break
print("".join(string))
