width_cake = int(input())
length_cake = int(input())

total_pieces = width_cake * length_cake
sum_pieces = 0
taken_pieces = input()
flag = False
while taken_pieces != "STOP":
    taken_pieces = int(taken_pieces)
    sum_pieces += taken_pieces

    if sum_pieces >= total_pieces:
        flag = True
        break

    taken_pieces = input()

    # if taken_pieces == "STOP":
    #     flag = True
    #     break

diff = abs(sum_pieces - total_pieces)
if flag:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")