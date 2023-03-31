dwarfs = {}
while True:
    line = input()
    if line == "Once upon a time":
        break

    line_args = line.split(" <:> ")

    name = line_args[0]
    color = line_args[1]
    physics = int(line_args[2])
    dwarfs[color] = dwarfs.get(color, {})
    dwarfs[color][name] = dwarfs[color].get(name, 0)
    if physics > dwarfs[color][name]:
        dwarfs[color][name] = physics

dwarfs_list = []
for hat_color in dwarfs.keys():
    for dwarf_name, points in dwarfs[hat_color].items():
        dwarfs_list.append({
            "length": len(dwarfs[hat_color]), "hat_color": hat_color, "dwarf_name": dwarf_name, "points": points
        })
for result in sorted(dwarfs_list, key=lambda x: (-x["points"], -x["length"])):
    print(f"({result['hat_color']}) {result['dwarf_name']} <-> {result['points']}")
