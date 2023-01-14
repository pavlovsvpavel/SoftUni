book_name = input()
counter = 0
while book_name != "No More Books":
    current_book = input()

    if current_book == book_name:
        print(f"You checked {counter} books and found it.")
        break

    counter += 1

    if current_book == "No More Books":
        counter -= 1
        print(f"The book you search is not here! \nYou checked {counter} books.")
        break

