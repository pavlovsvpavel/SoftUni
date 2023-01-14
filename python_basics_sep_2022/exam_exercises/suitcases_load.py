luggage_compartment_volume = float(input())

suitcase_volume = input()
total_volume = 0
count_suitcases = 0
flag = False
while suitcase_volume != "End":
    suitcase_volume = float(suitcase_volume)
    count_suitcases += 1

    if count_suitcases % 3 == 0:
        suitcase_volume = suitcase_volume * 1.1

    total_volume += suitcase_volume

    if total_volume > luggage_compartment_volume:
        count_suitcases -= 1
        flag = True
        break

    suitcase_volume = input()

if flag:
    print(f"No more space!\nStatistic: {count_suitcases} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {count_suitcases} suitcases loaded.")
