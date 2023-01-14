interval_start = int(input())
interval_end = int(input())
magick_number = int(input())

counter = 0
result = 0
flag = False
for i in range(interval_start, interval_end + 1):
    for j in range(interval_start, interval_end + 1):
        result = i + j
        counter += 1

        if result == magick_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{counter} ({i} + {j} = {magick_number})")
else:
    print(f"{counter} combinations - neither equals {magick_number}")
