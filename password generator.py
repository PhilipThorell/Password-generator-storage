from customtkinter import *
import json
import random


class GUI:

    def __init__(self, text: str, email: str, username: str, password: str, description: str) -> None:
        self.text = text
        self.email = email
        self.username = username
        self.password = password
        self.description = description
        self.frame = CTkFrame(window, width=780, height=700, fg_color="transparent")
        self.frame.place(x=320, y=0)
        self.button = CTkButton(scrollable_frame, text=text, font=("Consolas", 26), width=280, height=50)
        self.button.configure(command=self.frame.tkraise)
        self.button.pack(pady=(0, 10))

        self.text_label = CTkLabel(self.frame, text="Folder Name:", font=("Consolas", 29))
        self.text_label.place(x=160, y=110)
        self.text_entry = CTkEntry(self.frame, font=("Consolas", 25), width=300, height=50)
        self.text_entry.insert(0, self.text)
        self.text_entry.place(x=380, y=100)

        self.email_label = CTkLabel(self.frame, text="E-mail:", font=("Consolas", 29))
        self.email_label.place(x=240, y=215)
        self.email_entry = CTkEntry(self.frame, font=("Consolas", 25), width=300, height=50)
        self.email_entry.insert(0, self.email)
        self.email_entry.place(x=380, y=205)

        self.username_label = CTkLabel(self.frame, text="Username:", font=("Consolas", 29))
        self.username_label.place(x=210, y=320)
        self.username_entry = CTkEntry(self.frame, font=("Consolas", 25), width=300, height=50)
        self.username_entry.insert(0, self.username)
        self.username_entry.place(x=380, y=310)

        self.pass_label = CTkLabel(self.frame, text="Password:", font=("Consolas", 29))
        self.pass_label.place(x=210, y=425)
        self.pass_entry = CTkEntry(self.frame, font=("Consolas", 25), width=300, height=50)
        self.pass_entry.insert(0, self.password)
        self.pass_entry.place(x=380, y=415)

        self.description_textbox = CTkTextbox(self.frame, font=("Consolas", 20), width=500, height=70)
        self.description_textbox.insert("0.0", self.description)
        self.description_textbox.place(x=150, y=510)

        self.save_button = CTkButton(self.frame, text="Save", font=("Consolas", 30))
        self.save_button.configure(command=lambda: save_confirm(self))
        self.save_button.place(x=600, y=630)
        self.cancel_button = CTkButton(self.frame, text="Cancel", font=("Consolas", 30))
        self.cancel_button.configure(command=lambda: cancel(self))
        self.cancel_button.place(x=440, y=630)
        self.delete_button = CTkButton(self.frame, text="Delete", font=("Consolas", 30))
        self.delete_button.configure(command=lambda: delete(self))
        self.delete_button.place(x=40, y=630)


def save_new() -> None:
    if name_entry.get() != "" and password_entry.get() != "":
        GUI(name_entry.get(), "", "", password_entry.get(), "")

        data_base["data"].append({"name": name_entry.get(), "email": "", "username": "",
                                  "password": password_entry.get(), "description": ""})
        save_data_base(json_file, data_base)

        name_entry.delete(0, END)
        password_entry.delete(0, END)


def generate_password() -> None:
    password_entry.delete(0, END)
    characters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in range(16):
        option = random.randint(1, 3)
        if option == 1:
            password_entry.insert(i, characters[random.randint(0, 25)])
        elif option == 2:
            password_entry.insert(i, characters[random.randint(0, 25)].upper())
        elif option == 3:
            password_entry.insert(i, numbers[random.randint(0, 9)])


def save_data_base(file_path: str, data: dict) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


def load_data_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data


def delete_folder(self: GUI) -> None:
    for dictionary in data_base["data"]:
        if dictionary["name"] == self.text and dictionary["password"] == self.password:
            data_base["data"].remove(dictionary)
            with open(json_file, 'w') as file:
                json.dump(data_base, file, indent=2)

        self.frame.destroy()
        self.button.destroy()
        main_frame.tkraise()


def save_info(self: GUI) -> None:
    for i in data_base["data"]:
        if i["name"] == self.text and i["password"] == self.password:
            i["name"] = self.text_entry.get()
            i["email"] = self.email_entry.get()
            i["username"] = self.username_entry.get()
            i["password"] = self.pass_entry.get()
            i["description"] = self.description_textbox.get("0.0", END)

            self.text = self.text_entry.get()
            self.email = self.email_entry.get()
            self.username = self.username_entry.get()
            self.password = self.pass_entry.get()
            self.description = self.description_textbox.get("0.0", END)

            self.button.configure(text=self.text_entry.get())

    save_data_base(json_file, data_base)
    self.frame.tkraise()


def cancel(self: GUI) -> None:
    self.text_entry.delete(0, END)
    self.text_entry.insert(0, self.text)
    self.email_entry.delete(0, END)
    self.email_entry.insert(0, self.email)
    self.username_entry.delete(0, END)
    self.username_entry.insert(0, self.username)
    self.pass_entry.delete(0, END)
    self.pass_entry.insert(0, self.password)
    self.description_textbox.delete("0.0", END)
    self.description_textbox.insert("0.0", self.description)


def delete(self: GUI) -> None:
    delete_frame = CTkFrame(window, width=440, height=250, border_width=5,
                            border_color="#151515").place(x=375, y=225)
    CTkLabel(delete_frame, text="delete this?", font=("Consolas", 40),
             fg_color="transparent").place(x=460, y=250)
    CTkButton(delete_frame, text="Confirm", font=("Consolas", 36),
              command=lambda: delete_folder(self)).place(x=620, y=390)
    CTkButton(delete_frame, text="Cancel", font=("Consolas", 36), fg_color="red",
              command=self.frame.tkraise).place(x=420, y=390)


def save_confirm(self: GUI) -> None:
    save_frame = CTkFrame(window, width=440, height=250, border_width=5,
                          border_color="#151515").place(x=375, y=225)
    CTkLabel(save_frame, text="save this?", font=("Consolas", 40),
             fg_color="transparent").place(x=460, y=250)
    CTkButton(save_frame, text="Confirm", font=("Consolas", 36),
              command=lambda: save_info(self)).place(x=620, y=390)
    CTkButton(save_frame, text="Cancel", font=("Consolas", 36), fg_color="red",
              command=self.frame.tkraise).place(x=420, y=390)


set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

window = CTk()
window.geometry("1100x700")


main_frame = CTkFrame(window, width=780, height=700, fg_color="transparent")
main_frame.place(x=320, y=0)

CTkLabel(main_frame, text="Save as:", font=("Consolas", 29)).place(x=130, y=80)

name_entry = CTkEntry(main_frame, font=("Consolas", 25), width=340, height=50)
name_entry.place(x=290, y=70)

CTkLabel(main_frame, text="Password:", font=("Consolas", 29)).place(x=130, y=260)

password_entry = CTkEntry(main_frame, font=("Consolas", 25), width=340, height=50)
password_entry.place(x=290, y=250)

CTkButton(main_frame, text="Generate", font=("Consolas", 30), command=generate_password).place(x=330, y=330)

CTkButton(main_frame, text="Save New", font=("Consolas", 30), width=210, command=save_new).place(x=530, y=630)


sidebar_frame = CTkFrame(window, width=320, height=700)
sidebar_frame.place(x=0, y=0)

scrollable_frame = CTkScrollableFrame(sidebar_frame, width=300, height=500, fg_color="transparent")
scrollable_frame.place(x=0, y=90)

create_button = CTkButton(sidebar_frame, text="Create New +", font=("Consolas", 26), width=280, height=50)
create_button.configure(command=main_frame.tkraise)
create_button.place(x=20, y=625)


json_file: str = "data.json"
data_base: dict = load_data_base(json_file)

buttons: list = []
for i in data_base["data"]:
    buttons.append(GUI(i["name"], i["email"], i["username"], i["password"], i["description"]))

main_frame.tkraise()


window.mainloop()
