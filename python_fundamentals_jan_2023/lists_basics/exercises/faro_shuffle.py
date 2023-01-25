# https://en.wikipedia.org/wiki/Faro_shuffle

cards_deck = input().split(" ")
shuffles = int(input())

half_deck_length = int(len(cards_deck) / 2)
counter = 0

for _ in range(shuffles):
    counter = 0

    for position in range(1, len(cards_deck) - 1):
        if position % 2 != 0:
            cards_deck.insert(position, cards_deck.pop(half_deck_length + counter))
            counter += 1
        else:
            continue

print(cards_deck)
