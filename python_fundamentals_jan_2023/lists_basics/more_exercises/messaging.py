sequence = input().split(" ")
characters = [char for char in input()]

text_length = len(characters)
current_number = []
message = []
for number in sequence:
    sum_of_numbers = 0
    current_number = [int(x) for x in number]

    for num in current_number:
        sum_of_numbers += num

    if sum_of_numbers < text_length:
        message.append(characters.pop(sum_of_numbers))
    else:
        diff = sum_of_numbers - text_length
        message.append(characters.pop(diff))

print("".join(message))

