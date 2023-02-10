numbers = input().split(", ")
num_list = list(map(int, numbers))

start = 1
end = 10

while num_list:
    # if not num_list:
    #     break

    current_group = []
    for num in range(start, end + 1):
        current_group = list(filter(lambda x: x <= num, num_list))

    for number in current_group:
        num_list.remove(number)

    print(f"Group of {end}'s: {current_group}")

    start = 1 + end
    end += 10
