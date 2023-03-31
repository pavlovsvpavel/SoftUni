dwarfs = {}
flag = False
while True:
    line = input()
    if line == "Once upon a time":
        break

    line_args = line.split(" <:> ")

    name = line_args[0]
    color = line_args[1]
    physics = int(line_args[2])
    dwarfs[name] = dwarfs.get(name, {})
    dwarfs[name][color] = dwarfs[name].get(color, 0)
    if physics > dwarfs[name][color]:
        dwarfs[name][color] = physics

count_colors = {}
for key, value in dwarfs.items():
    for color in value.keys():
        if color in count_colors:
            count_colors[color] += 1
        else:
            count_colors[color] = count_colors.get(color, 1)
for value in count_colors.values():
    if value > 1:
        flag = True

if flag:
    for hat_color, value in sorted(count_colors.items(), key=lambda x: (-x[1], x[0])):
        for dwarf in dwarfs.keys():
            for name, points in sorted(dwarfs[dwarf].items(), key=lambda x: (-x[1], x[0])):
                if hat_color == name:
                    print(f"({name}) {dwarf} <-> {points}")
else:
    for dwarf, value in dwarfs.items():
        for name, points in sorted(value.items(), key=lambda x: (-x[1], x[0])):
            print(f"({name}) {dwarf} <-> {points}")
