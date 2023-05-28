import re

punctuations_pattern = r"[^\w\s]"
letters_pattern = r"[^\W\s]"
new_text = []

with open("files/text.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        punctuations_count = len(re.findall(punctuations_pattern, line))
        letters_count = len(re.findall(letters_pattern, line))

        new_line = f"Line {line_num}: {line.strip()} ({letters_count})({punctuations_count})\n"
        new_text.append(new_line)

with open("files/output.txt", "a") as output_file:
    output_file.writelines(new_text)
