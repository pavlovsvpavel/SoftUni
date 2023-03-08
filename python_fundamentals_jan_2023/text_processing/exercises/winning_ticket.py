def find_symbols(string, symbol):
    symbols_count = 0
    for pos, el in enumerate(string):
        if el == symbol:
            symbols_count += 1
            if pos + 1 < len(string):
                if string[pos + 1] != symbol:
                    break
    return symbols_count


tickets_collection = [x.strip() for x in input().split(", ")]
special_symbols = ['@', '#', '$', '^']

for ticket in tickets_collection:
    ticket_chars = len(ticket)
    if ticket_chars < 20:
        print("invalid ticket")
        continue
    half_ticket = ticket_chars // 2
    match_symbol = ""
    for special in special_symbols:
        if special in ticket:
            match_symbol = special

    left_half = ticket[:half_ticket]
    left_count = find_symbols(left_half, match_symbol)
    right_half = ticket[half_ticket:]
    right_count = find_symbols(right_half, match_symbol)

    if min(left_count, right_count) >= 10:
        print(f'ticket "{ticket}" - {min(left_count, right_count)}{match_symbol} Jackpot!')
    elif 6 <= min(left_count, right_count) < 10:
        print(f'ticket "{ticket}" - {min(left_count, right_count)}{match_symbol}')
    else:
        print(f'ticket "{ticket}" - no match')

