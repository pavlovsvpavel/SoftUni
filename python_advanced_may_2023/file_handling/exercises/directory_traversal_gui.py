import os
import re
import time
from collections import defaultdict
from tkinter import *
from tkinter import ttk


def change_on_hover(button, on_hover, on_leave):
    button.bind("<Enter>", func=lambda e: button.config(background=on_hover))
    button.bind("<Leave>", func=lambda e: button.config(background=on_leave))


def progress_steps():
    for x in range(5):
        progress_bar["value"] += 20
        app.update_idletasks()

        time.sleep(0.3)

        if progress_bar["value"] == 100:
            change_message()


def change_message():
    message_label["text"] = "Done"
    run_button["state"] = "disabled"


def reload():
    run_button["state"] = "active"
    message_label["text"] = ""
    progress_bar.stop()
    path_field.delete(0, END)
    file_field.delete(0, END)


def file_open(file):
    if not os.path.exists(file):
        message_label["text"] = "No such file"
    else:
        os.system(r'start ' + file)


def validation():
    if run():
        progress_steps()


def run():
    global message_label
    global output_file

    path = path_field.get()
    file_name_for_report = file_field.get()

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

    if not dict_files:
        message_label["text"] = "No such directory"
        return

    sorted_dict = dict(sorted(dict_files.items(), key=lambda x: (x[0], x[1])))

    with open(output_file, "a") as report:
        for key, values in sorted_dict.items():
            report.write(f"{key}\n")
            for c_file in sorted_dict[key]:
                report.write(f"- - - {c_file}\n")

    return output_file


output_file = ""

app = Tk()
app.title("Directory traversal")
app.geometry("300x220")
app.resizable(width=False, height=False)

path_field_text = Label(app, font="calibri", text="Enter path to folder:")
path_field_text.grid(row=0, column=0, sticky="w", padx=10)

path_field = Entry(app, font="calibri", width=30)
path_field.grid(row=1, column=0, sticky="w", padx=10)

file_field_text = Label(app, font="calibri", text="Enter name for output file:")
file_field_text.grid(row=2, column=0, sticky="w", padx=10)


file_field = Entry(app, font="calibri", width=25)
file_field.grid(row=3, column=0, sticky="w", padx=10)

file_extension = Label(app, font="calibri", text=".txt")
file_extension.place(x=220, y=75)

run_button = Button(app, font="calibri", text="Run", width=5, padx=15,
                    command=validation
                    )
run_button.place(x=10, y=130)
change_on_hover(run_button, "blue", "SystemButtonFace")

message_label = Label(app, font="calibri", fg="red")
message_label.place(x=10, y=100)

s = ttk.Style()
s.theme_use('alt')
s.configure("blue.Horizontal.TProgressbar", background='blue')
progress_bar = ttk.Progressbar(app, orient=HORIZONTAL, length=280,
                               mode="determinate",
                               style="blue.Horizontal.TProgressbar"
                               )
progress_bar.place(x=10, y=180)

clear_button = Button(app, font="calibri", text="Clear", width=5, padx=15,
                      command=reload
                      )
clear_button.place(x=110, y=130)
change_on_hover(clear_button, "red", "SystemButtonFace")

open_file = Button(app, font="calibri", text="Open file", width=5, padx=15,
                   command=lambda: file_open(output_file)
                   )
open_file.place(x=210, y=130)
change_on_hover(open_file, "green2", "SystemButtonFace")

app.mainloop()
