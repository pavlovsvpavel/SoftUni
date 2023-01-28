line_1 = [int(x) for x in input().split(" ")]
line_2 = [int(x) for x in input().split(" ")]
line_3 = [int(x) for x in input().split(" ")]

row_winner = []
column_winner = []
cross_winner = []
winner = []

if line_1[0] == line_1[1] == line_1[2]:
    row_winner = [line_1[0] + line_1[1] + line_1[2]]
elif line_2[0] == line_2[1] == line_2[2]:
    row_winner = [line_2[0] + line_2[1] + line_2[2]]
elif line_3[0] == line_3[1] == line_3[2]:
    row_winner = [line_3[0] + line_3[1] + line_3[2]]

if line_1[0] == line_2[0] == line_3[0]:
    column_winner = [line_1[0] + line_2[0] + line_3[0]]
elif line_1[1] == line_2[1] == line_3[1]:
    column_winner = [line_1[1] + line_2[1] + line_3[1]]
elif line_1[2] == line_2[2] == line_3[2]:
    column_winner = [line_1[2] + line_2[2] + line_3[2]]

if line_1[0] == line_2[1] == line_3[2]:
    cross_winner = [line_1[0] + line_2[1] + line_3[2]]
elif line_1[2] == line_2[1] == line_3[0]:
    cross_winner = [line_1[2] + line_2[1] + line_3[0]]

winner = row_winner + column_winner + cross_winner

if not winner or winner[0] == 0:
    print("Draw!")
elif winner[0] == 3:
    print("First player won")
elif winner[0] == 6:
    print("Second player won")