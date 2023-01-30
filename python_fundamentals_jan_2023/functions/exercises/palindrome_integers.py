def palindrome_numbers(number):
    numbers_list = [x for x in number.split(", ")]
    for num in numbers_list:
        single_number = [x for x in num]
        reversed_single_number = single_number[:: - 1]
        if reversed_single_number == single_number:
            print("True")
        else:
            print("False")


user_input = input()
palindrome_numbers(user_input)
