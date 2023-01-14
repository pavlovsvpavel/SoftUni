budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

amount_video_cards = video_cards_count * 250
amount_processors = processors_count * amount_video_cards * 0.35
amount_ram_memory = ram_memory_count * amount_video_cards * 0.1

all_amount = amount_video_cards + amount_processors + amount_ram_memory

if video_cards_count > processors_count:
    all_amount = all_amount - (all_amount * 0.15)
else:
    all_amount = all_amount

diff = (f"{abs(budget - all_amount):.2f}")

if all_amount <= budget:
    print(f"You have {diff} leva left!")
else:
    print(f"Not enough money! You need {diff} leva more!")
