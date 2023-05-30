import os
import re
from collections import defaultdict

path = input(r"Enter path to folder: ")
file_name_for_report = input("Enter file name: ")
output_file = os.path.join(path, file_name_for_report + ".txt")

dict_files = defaultdict(list)
pattern = r"\.[a-z]+$"

for (root, dirs, files) in os.walk(path):
    for file in files:
        f_extension = re.findall(pattern, file)
        file_path = os.path.join(root, file)
        size = os.stat(file_path).st_size / 1024

        # Minimum size set to 1 KB for files with fewer data
        if 0 < size < 1:
            size = 1

        dict_files[f_extension[0]].append(f"{file} - size: {size:,.0f} KB")

sorted_dict = dict(sorted(dict_files.items(), key=lambda x: (x[0], x[1])))

with open(output_file, "a") as report:
    for key, values in sorted_dict.items():
        report.write(f"{key}\n")
        for c_file in sorted_dict[key]:
            report.write(f"- - - {c_file}\n")
