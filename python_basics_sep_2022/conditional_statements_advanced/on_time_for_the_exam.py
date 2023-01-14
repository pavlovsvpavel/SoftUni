exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_total_min = exam_hour * 60 + exam_min
arrival_total_min = arrival_hour * 60 + arrival_min

total_diff_in_min = abs(exam_total_min - arrival_total_min)
diff_in_hours = total_diff_in_min // 60
diff_in_min = total_diff_in_min % 60

if arrival_total_min <= exam_total_min:
    if 0 < total_diff_in_min <= 30:
        print("On time")
        print(f"{diff_in_min} minutes before the start")
    elif 30 < total_diff_in_min < 60:
        print("Early")
        print(f"{diff_in_min} minutes before the start")
    elif total_diff_in_min >= 60:
        print("Early")
        print(f"{diff_in_hours}:{diff_in_min:02d} hours before the start")
    elif total_diff_in_min == 0:
        print("On time")
if arrival_total_min > exam_total_min:
    if total_diff_in_min < 60:
        print("Late")
        print(f"{diff_in_min} minutes after the start")
    elif total_diff_in_min >= 60:
        print("Late")
        print(f"{diff_in_hours}:{diff_in_min:02d} hours after the start")
