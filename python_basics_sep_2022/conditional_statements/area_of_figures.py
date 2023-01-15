from math import pi
figure_type = input("Enter type: ")
area = 0
wrong_input = True

if figure_type == "square":
    a = float(input("Enter side size: "))
    area = (a * a)
elif figure_type == "rectangle":
    a = float(input("Enter side size a: "))
    b = float(input("Enter side size b: "))
    area = (a * b)
elif figure_type == "circle":
    radius = float(input("Enter radius size: "))
    area = (radius ** 2) * pi
elif figure_type == "triangle":
    side = float(input("Enter side size: "))
    height = float(input("Enter height size: "))
    area = 1/2 * (side * height)
else:
    print("Wrong data!")
    wrong_input = False
if wrong_input:
    print(f"{area:.3f}")


