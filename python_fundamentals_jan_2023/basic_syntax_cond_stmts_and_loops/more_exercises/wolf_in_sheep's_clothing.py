string = input()

string_list = string.split(", ")
counter = 0
flag = False

for i in range(len(string_list) - 1, - 1, - 1):
    if string_list[len(string_list) - 1] == "wolf":
        break
    if string_list[i] == "wolf":
        flag = True
        break
    if string_list[i] == "sheep":
        counter += 1

if flag:
    print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
else:
    print("Please go away and stop eating my sheep")

