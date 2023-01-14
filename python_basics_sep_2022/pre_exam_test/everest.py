meters_goal = 8848
sum_of_meters = 5364
days_counter = 1

flag = False
rest = input()
while rest != "END":
    meters = int(input())

    if rest == "Yes":
        days_counter += 1
    if rest == "END":
        break
    if days_counter > 5:
        break

    sum_of_meters += meters

    if sum_of_meters >= meters_goal:
        flag = True
        break

    rest = input()

if flag:
    print(f"Goal reached for {days_counter} days!")
else:
    print(f"Failed!\n{sum_of_meters}")
