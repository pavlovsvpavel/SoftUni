to_do_list = []
while True:
    notes = input()
    if notes == "End":
        break

    command = notes.split("-")
    priority = int(command[0])
    task = command[1]
    to_do_list.append((priority, task))


result = [x[1] for x in sorted(to_do_list)]
print(result)


