detergent_bottles = int(input())
detergent_ml = detergent_bottles * 750

ml_per_dish = 5
ml_per_pot = 15
total_ml = 0
counter = 0
total_dishes = 0
total_pots = 0
input_line = input()
flag = False

while input_line != "End":
    input_line = int(input_line)
    counter += 1
    if counter % 3 != 0:
        total_ml += input_line * ml_per_dish
        total_dishes += input_line
    else:
        total_ml += input_line * ml_per_pot
        total_pots += input_line
    if total_ml > detergent_ml:
        flag = True
        break

    input_line = input()

diff = abs(total_ml - detergent_ml)

if flag:
    print(f"Not enough detergent, {diff} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
