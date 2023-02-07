rooms = int(input())
free_chairs = 0
needed_chairs = []
room_number = []
is_valid = True

for room in range(1, rooms + 1):
    current_info = input().split(" ")
    chairs = [x for x in current_info[0]].count("X")
    visitors = int(current_info[1])

    if chairs >= visitors:
        free_chairs += chairs - visitors

    elif chairs < visitors:
        needed_chairs.append(abs(chairs - visitors))
        room_number.append(room)
        is_valid = False

if free_chairs >= 0 and is_valid:
    print(f"Game On, {free_chairs} free chairs left")

for i in range(len(needed_chairs)):
    print(f"{needed_chairs[i]} more chairs needed in room {room_number[i]}")
