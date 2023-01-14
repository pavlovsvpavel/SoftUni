import sys
player_one_eggs = int(input())
player_two_eggs = int(input())

for i in range(sys.maxsize):
    winner = input()

    if winner == "one":
        player_two_eggs -= 1
    elif winner == "two":
        player_one_eggs -= 1
    else:
        print(f"Player one has {player_one_eggs} eggs left.")
        print(f"Player two has {player_two_eggs} eggs left.")
        break

    if player_one_eggs == 0:
        print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
        break
    elif player_two_eggs == 0:
        print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
        break


