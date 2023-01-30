user_password = input()


def password_validator(password):
    password_elements = [x for x in password]
    is_valid = True
    # Checks the length of password
    if 6 > len(password_elements) or len(password_elements) > 10:
        print(f"Password must be between 6 and 10 characters")
        is_valid = False
    # Checks for digits and letters in password
    digits_counter = 0
    letters_counter = 0

    for element in password_elements:
        if element.isdigit():
            digits_counter += 1
        if element.isalpha():
            letters_counter += 1

    if digits_counter + letters_counter != len(password_elements):
        print(f"Password must consist only of letters and digits")
        is_valid = False

    if digits_counter < 2:
        print(f"Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")

    return


password_validator(user_password)

