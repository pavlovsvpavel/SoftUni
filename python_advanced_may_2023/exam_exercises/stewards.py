from collections import deque

seats = input().split(", ")
first = deque(int(x) for x in input().split(", "))
second = deque(int(x) for x in input().split(", "))

matches = []
rotations = 0

while True:
    if len(matches) == 3 or rotations == 10:
        break

    first_num = first.popleft()
    second_num = second.pop()
    sum_numbers = first_num + second_num

    letter = chr(sum_numbers)

    searched_seats = [str(first_num) + letter, str(second_num) + letter]

    for s_seat in searched_seats:
        if s_seat in seats:
            matches.append(s_seat)
            seats.remove(s_seat)
            break

    else:
        first.append(first_num)
        second.appendleft(second_num)

    rotations += 1

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotations}")
