import re

text = input()
cool_threshold = 1
for char in text:
    if char.isdigit():
        char = int(char)
        cool_threshold *= char
pattern = r"(::|\*\*)(?P<emoji>[A-Z][a-z]{2,})\1"
matches = re.finditer(pattern, text)
emoji_dict = {}
for match in matches:
    emoji_dict[match.group()] = match["emoji"]

for emoji, value in emoji_dict.items():
    coolness = 0
    for char in value:
        coolness += ord(char)
    if coolness < cool_threshold:
        emoji_dict[emoji] = ""

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_dict)} emojis found in the text. The cool ones are:")
for emoji, value in emoji_dict.items():
    if value:
        print(f"{emoji}")
