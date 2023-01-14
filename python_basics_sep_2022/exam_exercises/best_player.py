player_name = input()
scored_goals = int(input())

best_player = ""
best_goals = 0
hat_trick = 0

while True:
    if scored_goals > best_goals:
        best_goals = scored_goals
        best_player = player_name

    if scored_goals >= 3:
        hat_trick = 1
        if scored_goals >= 10:
            break

    player_name = input()

    if player_name == "END":
        break
    scored_goals = int(input())

print(f"{best_player} is the best player!")

if hat_trick == 1:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")


