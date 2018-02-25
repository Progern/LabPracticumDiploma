from tkinter import *  # Import all packages from tkinter

from utils.login_utils import check_name_valid
from windows import main_app_window

rootWindow = Tk()  # Creates a blank window
rootWindow.title("Лабораторний практикум")

rootFrame = Frame(rootWindow, width=500, height=200)
rootFrame.pack()


def create_widgets():
    label_user_name = Label(rootFrame, text="Введіть ваше ім'я")
    label_invalid_user_name = Label(rootFrame, text="Ім'я повинно бути довшим за 5 символів", fg="red")

    input_field_user_name = Entry(rootFrame)

    confirmation_button = Button(rootFrame, text="Підтвердити",
                                 command=lambda: perform_login(input_field_user_name.get(),
                                                               label_invalid_user_name))

    statistics_check_box = Checkbutton(rootFrame, text="Зберігати статистику?")
    pack_widgets(label_user_name, input_field_user_name, confirmation_button, statistics_check_box)


def pack_widgets(label_user_name, input_field_user_name, confirmation_button, statisticks_check_box):
    label_user_name.grid(row=0, column=0)

    input_field_user_name.grid(row=2, column=0)

    confirmation_button.grid(row=3, column=0)

    statisticks_check_box.grid(columnspan=2)  # This checkbox with text will take two columns

    rootWindow.mainloop()


def perform_login(name, label_invalid_user_name):
    if check_name_valid(name):
        label_invalid_user_name.grid_forget()
        rootWindow.destroy()
        main_app_window._init_()
        return

    label_invalid_user_name.grid(row=1, column=0)


create_widgets()
