def lift_check(lst):
    counter = 0
    for x in lst:
        if int(x) != max_people_per_wagon:
            counter += 1
    if counter > 0:
        return False
    else:
        return True


people_count = int(input())
lift_state = input()
max_people_per_wagon = 4
wagon_list = [int(x) for x in (lift_state.split(" "))]
new_wagon_list = []

for index in wagon_list:
    if people_count == 0:
        new_wagon_list.append(str(index))
    elif index == 0:
        if people_count >= max_people_per_wagon:
            new_wagon_list.append(str(max_people_per_wagon))
            people_count -= max_people_per_wagon
        else:
            new_wagon_list.append(str(people_count))
            people_count -= people_count

    else:
        if people_count < max_people_per_wagon:
            sum_of_people = index + people_count
            new_wagon_list.append(str(sum_of_people))
            people_count -= people_count
        else:
            new_wagon_list.append(str(max_people_per_wagon))
            people_count -= (max_people_per_wagon - index)

if lift_check(new_wagon_list) and people_count == 0:
    print(" ".join(new_wagon_list))
elif people_count == 0:
    print("The lift has empty spots!")
    print(" ".join(new_wagon_list))
else:
    print(f"There isn't enough space! {people_count} people in a queue!")
    print(" ".join(new_wagon_list))


