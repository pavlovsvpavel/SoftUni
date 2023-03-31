all_players = {}
while True:
    line = input()
    if line == "Season end":
        break

    if "->" in line:
        line_args = line.split(" -> ")
        player_name = line_args[0]
        position = line_args[1]
        skill = int(line_args[2])
        if player_name in all_players.keys():
            if position not in all_players[player_name].keys():
                all_players[player_name][position] = skill
            else:
                if all_players[player_name][position] < skill:
                    all_players[player_name][position] = skill
        else:
            all_players[player_name] = {position: skill}

    elif "vs" in line:
        line_args = line.split(" vs ")
        player_1 = line_args[0]
        player_2 = line_args[1]
        if player_1 in all_players.keys() and player_2 in all_players.keys():
            for first in all_players[player_1].keys():
                for second in all_players[player_2].keys():
                    if first == second:
                        if all_players[player_1][first] > all_players[player_2][second]:
                            all_players[player_2][second] = 0
                        else:
                            all_players[player_1][first] = 0

players_total_skill = {}
for key, value in all_players.items():
    players_total_skill[key] = sum(value.values())

for name, total_points in sorted(players_total_skill.items(), key=lambda x: (-x[1], x[0])):
    if total_points > 0:
        print(f"{name}: {total_points} skill")
        for pos, points in sorted(all_players[name].items(), key=lambda x: (-x[1], x[0])):
            print(f"- {pos} <::> {points}")
