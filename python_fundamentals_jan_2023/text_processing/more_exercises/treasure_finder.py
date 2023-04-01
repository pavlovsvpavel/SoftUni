import re

key = [int(x) for x in input().split(" ")]
while True:
    some_string = input()
    if some_string == "find":
        break
    index = 0
    decrypted_message = ""
    for char in some_string:
        if index >= len(key):
            index = 0
        new_char = ord(char) - key[index]
        decrypted_message += chr(new_char)
        index += 1
    # type_pattern = r"&([A-Za-z]+)&"
    # coordinates_pattern = r"<([A-Za-z\d]+)>"
    # treasure_type = re.findall(type_pattern, decrypted_message)
    # coordinates = re.findall(coordinates_pattern, decrypted_message)
    # print(f"Found {treasure_type[0]} at {coordinates[0]}")
    pattern = r"&([A-Za-z]+)&(\w+)<([A-Za-z\d]+)>"
    matches = re.findall(pattern, decrypted_message)
    print(f"Found {matches[0][0]} at {matches[0][2]}")
