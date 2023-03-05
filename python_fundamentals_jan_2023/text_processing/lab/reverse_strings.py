while True:
    text = input()

    if text == "end":
        break

    reversed_text = "".join(list(reversed(text)))

    print(f"{text} = {reversed_text}")
