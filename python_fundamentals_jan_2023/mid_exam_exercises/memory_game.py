def check_for_match(lst):
    if lst[command_lst[0]] == lst[command_lst[1]]:
        element = lst[command_lst[0]]
        return element


def cheat_check(lst, el_lst):
    is_cheat = False
    if lst[0] == lst[1]:
        is_cheat = True
    elif lst[0] < 0 or lst[1] < 0:
        is_cheat = True
    elif lst[0] > len(el_lst) - 1 or lst[1] > len(el_lst) - 1:
        is_cheat = True
    return is_cheat


def win_lose(lst):
    if lst:
        return False
    else:
        return True


elements = input()
command = input()
ele_lst = [x for x in elements.split(" ")]
moves = 0

while command != "end":
    command_lst = [int(x) for x in command.split(" ")]
    moves += 1
    if cheat_check(command_lst, ele_lst):
        ele_lst = ele_lst[:(len(ele_lst) // 2)] + 2 * [f"-{moves}a"] + ele_lst[(len(ele_lst) // 2):]
        print("Invalid input! Adding additional elements to the board")
    elif check_for_match(ele_lst):
        print(f"Congrats! You have found matching elements - {check_for_match(ele_lst)}!")
        ele_lst = list(filter(lambda x: x != check_for_match(ele_lst), ele_lst))
    else:
        print("Try again!")
    if win_lose(ele_lst):
        print(f"You have won in {moves} turns!")
        break

    command = input()

if not win_lose(ele_lst):
    print("Sorry you lose :(")
    print(" ".join(ele_lst))
