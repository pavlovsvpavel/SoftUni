x = float(input())
y = float(input())
h = float(input())

back_wall_area = x * x
door_area = 1.2 * 2
front_wall_area = (x * x) - door_area
window_area = 1.5 * 1.5
side_wall_left_area = (x * y) - window_area
side_wall_right_area = (x * y) - window_area
total_area_lower_part = back_wall_area + front_wall_area + side_wall_right_area + side_wall_left_area

roof_sides = 2 * (x * y)
roof_base = 2 * (1 / 2 * x * h)
total_roof_area = roof_base + roof_sides

green_paint_qty = total_area_lower_part / 3.4
red_paint_qty = total_roof_area / 4.3

print(f"{green_paint_qty:.2f}")
print(f"{red_paint_qty:.2f}")