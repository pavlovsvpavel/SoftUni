import re
import os

directory_name = input("Enter directory name for output files: ")
file_name = input("Enter name for output file: ")

absolute_path = os.path.abspath(os.path.dirname(__file__))
new_directory_path = os.path.join(absolute_path, directory_name)
output_file_path = os.path.join(new_directory_path, file_name + ".txt")

try:
    os.mkdir(new_directory_path)

except FileExistsError:
    pass

punctuations_pattern = r"[^\w\s]"
letters_pattern = r"[^\W\s]"
new_text = []

with open("text.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        punctuations_count = len(re.findall(punctuations_pattern, line))
        letters_count = len(re.findall(letters_pattern, line))

        new_line = f"Line {line_num}: {line.strip()} ({letters_count})({punctuations_count})\n"
        new_text.append(new_line)

with open(output_file_path, "w") as output_file:
    output_file.writelines(new_text)
