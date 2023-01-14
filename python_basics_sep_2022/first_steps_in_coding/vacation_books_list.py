number_of_pages = int(input())
pages_per_hour = int(input())
days_to_finish = int(input())
total_hours = number_of_pages // pages_per_hour
hours_per_day = total_hours / days_to_finish
print(hours_per_day)
