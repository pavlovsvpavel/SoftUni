from math import floor
tournaments_count = int(input())
init_points = int(input())

final_points = init_points
count_wins = 0
for _ in range(1, tournaments_count + 1):
    tournament_stage = input()
    if tournament_stage == "W":
        count_wins += 1
        tournament_points = 2000
        final_points += tournament_points
    elif tournament_stage == "F":
        tournament_points = 1200
        final_points += tournament_points
    elif tournament_stage == "SF":
        tournament_points = 720
        final_points += tournament_points

average_points_per_tournament = floor((final_points - init_points) / tournaments_count)
percent_wins = (count_wins / tournaments_count) * 100
print(f"Final points: {final_points}")
print(f"Average points: {average_points_per_tournament}")
print(f"{percent_wins:.2f}%")

