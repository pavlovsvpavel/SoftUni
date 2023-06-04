import re
import tkinter as tk


# function to change properties of button on hover
def change_on_hover(button, on_hover, on_leave):
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(background=on_hover))

    # background color on leaving widget
    button.bind("<Leave>", func=lambda e: button.config(background=on_leave))


def enter(event):
    email_validation()
    input_field.delete(0, "end")


def email_validation():
    global message_label

    name_pattern = r"^[\w\.\-]{5,}@"
    domain_pattern = r"\.com$|\.bg$|\.net$|\.org$"
    message = ""
    color = "red"

    symbol_counter = input_field.get().count("@")
    name_validator = bool(re.search(name_pattern, input_field.get()))
    domain_validator = bool(re.search(domain_pattern, input_field.get()))

    if not input_field.get():
        message = "Empty field"

    elif name_validator and symbol_counter == 1 and domain_validator:
        message = "Email is valid!"
        color = "green"

    elif not symbol_counter:
        message = "Email must contain '@'!"

    elif not name_validator:
        message = "Name must be more than 4 characters!"

    elif symbol_counter > 1:
        message = "Email must contain only one '@' symbol!"

    elif not domain_validator:
        message = "Domain must be one of the following:\n.com, .bg, .org, .net!"

    message_label.config(text=message, fg=color)
    user_email.config(text=input_field.get())
    input_field.delete(0, "end")


app = tk.Tk()
app.title("Email Validator")
app.geometry("350x170")

input_field_text = tk.Label(font="calibri", text="Please enter your email:")
input_field_text.place(x=15, y=8)

input_field = tk.Entry(app, font="calibri")
input_field.bind("<Return>", enter)
input_field.place(x=15, y=40, height=25, width=200)

validation_button = tk.Button(app, font="calibri", text="Check", height=1, padx=15, command=email_validation)
validation_button.place(x=240, y=35)
change_on_hover(validation_button, "DeepSkyBlue", "SystemButtonFace")

message_label = tk.Label(app, font="calibri")
message_label.place(x=15, y=100)

user_email = tk.Label(app, font=("calibri", 12), fg="black")
user_email.place(x=15, y=80)

app.mainloop()
