width = float(input())
length = float(input())

one_working_place_length = 70
one_working_place_width = 120
hallway_area_length = 100
door_area = 1
console_area = 2
wrong_input = True

if 3 <= length <= width <= 100:
    total_length_area = length * 100 - hallway_area_length
    working_spaces_length = (total_length_area // one_working_place_length)
    total_width_area = width * 100
    working_spaces_width = (total_width_area // one_working_place_width)
    working_spaces_count = working_spaces_width * working_spaces_length - door_area - console_area
else:
    print("Wrong input!")
    wrong_input = False
if wrong_input:
    print(working_spaces_count)
