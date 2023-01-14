movie_name = input()

count_student = 0
count_standard = 0
count_kid = 0
count_all_tickets = 0
flag = False

while movie_name != "Finish":
    free_seats = int(input())
    count_tickets_per_movie = 0

    while True:
        if count_tickets_per_movie == free_seats:
            flag = True
            break

        ticket_type = input()

        if ticket_type == "End":
            flag = True
            break

        if ticket_type == "student":
            count_student += 1
            count_tickets_per_movie += 1
        elif ticket_type == "standard":
            count_standard += 1
            count_tickets_per_movie += 1
        elif ticket_type == "kid":
            count_kid += 1
            count_tickets_per_movie += 1

        count_all_tickets += 1

    if flag:
        print(f"{movie_name} - {count_tickets_per_movie / free_seats * 100:.2f}% full.")

    movie_name = input()

print(f"Total tickets: {count_all_tickets}")
print(f"{count_student / count_all_tickets * 100:.2f}% student tickets.")
print(f"{count_standard / count_all_tickets * 100:.2f}% standard tickets.")
print(f"{count_kid / count_all_tickets * 100:.2f}% kids tickets.")


