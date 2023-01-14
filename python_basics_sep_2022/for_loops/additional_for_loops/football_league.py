stadium_capacity = int(input())
fans_count = int(input())

a_count = 0
b_count = 0
v_count = 0
g_count = 0
for _ in range(1, fans_count + 1):
    sector = input()
    if sector == "A":
        a_count += 1
    elif sector == "B":
        b_count += 1
    elif sector == "V":
        v_count += 1
    elif sector == "G":
        g_count += 1

percent_filled = fans_count / stadium_capacity * 100
print(f"{a_count / fans_count * 100:.2f}%")
print(f"{b_count / fans_count * 100:.2f}%")
print(f"{v_count / fans_count * 100:.2f}%")
print(f"{g_count / fans_count * 100:.2f}%")
print(f"{percent_filled:.2f}%")
