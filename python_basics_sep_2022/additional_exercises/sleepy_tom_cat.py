holidays = int(input())

total_days_in_year = 365
total_play_time_year = 30000
time_in_hours_year = total_play_time_year // 60
time_in_minutes_year = total_play_time_year % 60

yearly_working_days = total_days_in_year - holidays

workday_time_for_play = yearly_working_days * 63
holiday_time_for_play = holidays * 127

total_play_time_actual = workday_time_for_play + holiday_time_for_play
diff = abs(total_play_time_year - total_play_time_actual)
time_in_hours = diff // 60
time_in_minutes = diff % 60

if total_play_time_actual >= total_play_time_year:
    print(f"Tom will run away\n{time_in_hours} hours and {time_in_minutes} minutes more for play")
else:
    print(f"Tom sleeps well\n{time_in_hours} hours and {time_in_minutes} minutes less for play")
