tickets_collection = [x.strip() for x in input().split(", ")]

special_symbols = ['@', '#', '$', '^']

for ticket in tickets_collection:
    ticket_chars = len(ticket)
    if ticket_chars < 20:
        print("invalid ticket")
        continue
    half_ticket = ticket_chars // 2
    left_side = 0
    left_half = ticket[:half_ticket]
    right_side = 0
    right_half = ticket[half_ticket:]
    match_symbol = ""
    for special in special_symbols:
        if special in ticket:
            match_symbol = special

    for pos, el in enumerate(left_half):
        if el == match_symbol:
            left_side += 1
            if pos + 1 < len(left_half):
                if left_half[pos + 1] != match_symbol:
                    break

    for pos, el in enumerate(right_half):
        if el == match_symbol:
            right_side += 1
            if pos + 1 < len(right_half):
                if right_half[pos + 1] != match_symbol:
                    break

    if min(left_side, right_side) >= 10:
        print(f'ticket "{ticket}" - {min(left_side, right_side)}{match_symbol} Jackpot!')
    elif 6 <= min(left_side, right_side) < 10:
        print(f'ticket "{ticket}" - {min(left_side, right_side)}{match_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')

