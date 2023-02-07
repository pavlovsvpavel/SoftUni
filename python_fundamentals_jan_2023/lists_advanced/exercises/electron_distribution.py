electrons = int(input())
shells = []
shell_num = 0

while True:
    if electrons <= 0:
        break

    shell_num += 1
    shells.append(shell_num)
    electrons_in_current_shell = 2 * (shell_num ** 2)
    if electrons_in_current_shell <= electrons:
        shells[shell_num - 1] = electrons_in_current_shell
    else:
        shells[shell_num - 1] = electrons

    electrons -= electrons_in_current_shell

print(shells)

