red_cards = input()

number_of_players = 11
team_a = []
team_b = []
card_check = []
player_number = []
less_players = False
for player in range(1, number_of_players + 1):
    team_a.append(str(player))
    team_b.append(str(player))

if "A" not in red_cards and "B" not in red_cards:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    exit()

cards_list = red_cards.split(" ")

# Checking every red card and remove player from team
for card_check in cards_list:
    player_number = card_check.split("-")

    if player_number[1] not in team_a or player_number[1] not in team_b:
        continue

    if "A" in card_check:
        team_a.remove(player_number[1])
    elif "B" in card_check:
        team_b.remove(player_number[1])
    else:
        continue

    if len(team_a) < 7 or len(team_b) < 7:
        less_players = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if less_players:
    print("Game was terminated")
