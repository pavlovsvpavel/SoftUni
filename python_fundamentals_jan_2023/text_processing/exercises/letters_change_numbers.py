from string import ascii_letters
main_string = [x.strip() for x in input().split(" ")]

alphabet = ascii_letters.upper()
total_result = 0
for el in main_string:
    el_length = len(el)
    if el_length == 0:
        continue
    start_letter = el[0]
    start_position = alphabet.index(start_letter.upper()) + 1
    end_letter = el[-1]
    end_position = alphabet.index(end_letter.upper()) + 1
    current_result = 0
    number = int(el[1:el_length - 1])
    if start_letter.isupper():
        current_result = number / start_position
    elif start_letter.islower():
        current_result = number * start_position
    if end_letter.isupper():
        current_result -= end_position
    elif end_letter.islower():
        end_letter.isupper()
        current_result += end_position

    total_result += current_result

print(f"{total_result:.2f}")
