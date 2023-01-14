count_groups = int(input())

total_people = 0
musala_sum = 0
monblan_sum = 0
kilimanjaro_sum = 0
k2_sum = 0
everest_sum = 0

for i in range(1, count_groups + 1):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala_sum += people_in_group
        total_people += people_in_group
    elif people_in_group <= 12:
        monblan_sum += people_in_group
        total_people += people_in_group
    elif people_in_group <= 25:
        kilimanjaro_sum += people_in_group
        total_people += people_in_group
    elif people_in_group <= 40:
        k2_sum += people_in_group
        total_people += people_in_group
    elif people_in_group >= 41:
        everest_sum += people_in_group
        total_people += people_in_group

percent_musala = musala_sum / total_people * 100
percent_monblan = monblan_sum / total_people * 100
percent_kilimanjaro = kilimanjaro_sum / total_people * 100
percent_k2 = k2_sum / total_people * 100
percent_everest = everest_sum / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

