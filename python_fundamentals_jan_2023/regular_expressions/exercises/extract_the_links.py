import re

while True:
    input_text = input()

    pattern = r"www\.[a-zA-Z0-9\-]+\.[\.a-z]+"

    if input_text:
        result = re.findall(pattern, input_text)
        if result:
            print("".join(result))
    else:
        break
