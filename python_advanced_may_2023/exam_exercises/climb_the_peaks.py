from collections import deque


def conquer(power, dictionary):
    for name, level in dictionary.items():
        if power >= level:
            return name
        else:
            return


def print_peaks(peaks_list):
    print("Conquered peaks:")
    print('\n'.join(peaks_list))


food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70,
}

total_peaks = len(peaks)
conquered_peaks = []
DAYS = 7

for _ in range(DAYS):
    current_food = food.pop()
    current_stamina = stamina.popleft()
    sum_of_food_and_stamina = current_food + current_stamina

    peak_name = conquer(sum_of_food_and_stamina, peaks)

    if peak_name:
        conquered_peaks.append(peak_name)
        del peaks[peak_name]


if len(conquered_peaks) == total_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print_peaks(conquered_peaks)

elif len(conquered_peaks) < total_peaks:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_peaks:
        print_peaks(conquered_peaks)
