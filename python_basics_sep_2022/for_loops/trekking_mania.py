count_groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_people = 0

for i in range(1, count_groups + 1):
    count_people_in_group = int(input())
    total_people += count_people_in_group
    if count_people_in_group <= 5:
        musala_count += count_people_in_group
    elif count_people_in_group <= 12:
        monblan_count += count_people_in_group
    elif count_people_in_group <= 25:
        kilimanjaro_count += count_people_in_group
    elif count_people_in_group <= 40:
        k2_count += count_people_in_group
    elif count_people_in_group >= 41:
        everest_count += count_people_in_group

print(f"{musala_count / total_people * 100:.2f}%")
print(f"{monblan_count / total_people * 100:.2f}%")
print(f"{kilimanjaro_count / total_people * 100:.2f}%")
print(f"{k2_count / total_people * 100:.2f}%")
print(f"{everest_count / total_people * 100:.2f}%")
