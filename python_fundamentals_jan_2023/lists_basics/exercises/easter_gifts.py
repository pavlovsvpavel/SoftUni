gifts_list = input().split()

while True:
    command_list = input().split()

    if "Money" in command_list:
        break

    if "OutOfStock" in command_list:
        if command_list[1] in gifts_list:
            while command_list[1] in gifts_list:
                gift_name = gifts_list.index(command_list[1])
                gifts_list = gifts_list[:gift_name] + ["None"] + gifts_list[gift_name + 1:]
                continue

    elif "Required" in command_list:
        if 0 < int(command_list[2]) < (len(gifts_list) - 1):
            gifts_list = gifts_list[:int(command_list[2])] + [command_list[1]] + gifts_list[int(command_list[2]) + 1:]

    elif "JustInCase" in command_list:
        gifts_list.pop()
        gifts_list.insert(len(gifts_list), command_list[1])

result = []
for i in gifts_list:
    if "None" != i:
        result.append(i)

print(" ".join(result))
