red_cards = input()

number_of_players = 11
team_a = []
team_b = []
less_players = False

for player in range(1, number_of_players + 1):
    team_a.append(player)
    team_b.append(player)

if "A" not in red_cards and "B" not in red_cards:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    exit()

cards_list = red_cards.split()

# Checking every red card and remove player from team
for i in cards_list:
    card_check = i.split("-")
    team = card_check[0]
    player_number = int(card_check[1])

    if team == "A":
        if player_number in team_a:
            team_a.remove(player_number)
    elif team == "B":
        if player_number in team_b:
            team_b.remove(player_number)

    if len(team_a) < 7 or len(team_b) < 7:
        less_players = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if less_players:
    print("Game was terminated")
