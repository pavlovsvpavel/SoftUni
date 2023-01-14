count_numbers = int(input())
message = ""

for _ in range(count_numbers):
    num_code = int(input())

    if num_code == 88:
        message = "Hello"
    elif num_code == 86:
        message = "How are you?"
    elif num_code < 88 and num_code != 86:
        message = "GREAT!"
    else:
        message = "Bye."

    print(message)
