import os
import re
import time
from collections import defaultdict
import tkinter as tk
from tkinter import ttk


def change_on_hover(button, on_hover, on_leave):
    button.bind("<Enter>", func=lambda e: button.config(background=on_hover))
    button.bind("<Leave>", func=lambda e: button.config(background=on_leave))


def progress_bar_steps():
    for x in range(5):
        progress_bar["value"] += 20
        app.update_idletasks()

        time.sleep(0.3)

        if progress_bar["value"] == 100:
            change_message()


def change_message():
    message_label.config(text="Done", fg="green")
    run_button["state"] = "disabled"


def clear_content():
    run_button["state"] = "active"
    open_file["state"] = "disabled"
    message_label.config(text="", fg="red")
    progress_bar.stop()
    path_field.delete(0, "end")
    file_field.delete(0, "end")
    levels_field.delete(0, "end")


def file_open(file):
    if not os.path.exists(file):
        message_label.config(text="No such file!")
    else:
        os.system(r'start ' + file)


def validation():
    if run():
        open_file["state"] = "normal"
        progress_bar_steps()


def run():
    global message_label
    global output_file

    path = path_field.get()
    file_name_for_report = file_field.get()

    if not file_name_for_report:
        file_name_for_report = "report"

    output_file = os.path.join(path, file_name_for_report + ".txt")

    dict_files = defaultdict(list)
    pattern = r"\.[a-z]+$"
    search_level = levels_field.get()  # specify in how many levels to search

    try:
        search_level = int(search_level)
    except ValueError:
        message_label.config(text="Enter a valid number!")
        return

    count_levels = -1

    for (root, dirs, files) in os.walk(path):
        count_levels += 1

        for file in files:
            f_extension = re.findall(pattern, file)
            file_path = os.path.join(root, file)
            size = os.stat(file_path).st_size / 1024

            # Minimum size set to 1 KB for files with fewer data
            if 0 < size < 1:
                size = 1

            dict_files[f_extension[0]].append(f"{file} - size: {size:,.0f} KB")

        if count_levels == search_level:
            break

    if not dict_files:
        message_label.config(text="No such file or directory!")
        return

    sorted_dict = dict(sorted(dict_files.items(), key=lambda x: (x[0], x[1])))

    with open(output_file, "a") as report:
        for key, values in sorted_dict.items():
            report.write(f"{key}\n")
            for c_file in sorted_dict[key]:
                report.write(f"- - - {c_file}\n")

    return output_file


output_file = ""
color = "red"

app = tk.Tk()
app.title("Directory Traversal")
app.geometry("300x350")
app.resizable(False, False)

levels_text = tk.Label(app, font=("calibri", 12), text="Specify in how many levels to search:")
levels_text.place(x=10, y=0)

levels_field = tk.Entry(app, font=("calibri", 12), width=15)
levels_field.place(x=10, y=30)

levels_text_example = tk.Label(app, font=("calibri", 9), text="Example: 0 for root, 1 for first level and etc.")
levels_text_example.place(x=10, y=55)

path_field_text = tk.Label(app, font=("calibri", 12), text="Enter full path to folder:")
path_field_text.place(x=10, y=90)

path_field = tk.Entry(app, font="calibri", width=30)
path_field.place(x=10, y=120)

path_example_text = tk.Label(app, font=("calibri", 9), text="Example: C:\Desktop\Folder")
path_example_text.place(x=10, y=145)

file_field_text = tk.Label(app, font=("calibri", 12), text="Enter name for output file:")
file_field_text.place(x=10, y=180)

file_field = tk.Entry(app, font="calibri", width=25)
file_field.place(x=10, y=210)

file_extension = tk.Label(app, font="calibri", text=".txt")
file_extension.place(x=220, y=210)

message_label = tk.Label(app, font="calibri", fg=color)
message_label.place(x=10, y=240)

run_button = tk.Button(app, font="calibri", text="Run", width=5, padx=15,
                       command=validation
                       )
run_button.place(x=10, y=270)
change_on_hover(run_button, "grey", "SystemButtonFace")

clear_button = tk.Button(app, font="calibri", text="Clear", width=5, padx=15,
                         command=clear_content
                         )
clear_button.place(x=110, y=270)
change_on_hover(clear_button, "grey", "SystemButtonFace")

open_file = tk.Button(app, font="calibri", text="Open file", width=5, padx=15,
                      command=lambda: file_open(output_file)
                      )
open_file.place(x=210, y=270)
change_on_hover(open_file, "grey", "SystemButtonFace")
open_file["state"] = "disabled"

s = ttk.Style()
s.theme_use('alt')
s.configure("blue.Horizontal.TProgressbar", background='blue')
progress_bar = ttk.Progressbar(app, orient="horizontal", length=280,
                               mode="determinate",
                               style="blue.Horizontal.TProgressbar"
                               )
progress_bar.place(x=10, y=320)

app.mainloop()
