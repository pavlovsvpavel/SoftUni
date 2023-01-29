sequence = input().split(" ")
characters = [char for char in input()]

text_length = len(characters)
current_number = []
message = []
for number in sequence:
    current_number = [int(x) for x in number]

    sum_of_numbers = sum(current_number)

    if sum_of_numbers < text_length:
        message.append(characters.pop(sum_of_numbers))
    else:
        diff = sum_of_numbers - text_length
        message.append(characters.pop(diff))

print("".join(message))

