import re

while True:
    input_text = input()

    pattern = r"(www\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

    if input_text:
        result = re.finditer(pattern, input_text)
        if result:
            for el in result:
                print("".join(el[0]))
    else:
        break
