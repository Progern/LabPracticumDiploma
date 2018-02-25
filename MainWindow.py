from tkinter import *  # Import all packages from tkinter

rootWindow = Tk()  # Creates a blank window
rootWindow.title("Лабораторний практикум")


def create_widgets():
    label_user_name = Label(rootWindow, text="Введіть ваше ім'я")
    label_invalid_user_name = Label(rootWindow, text="Ім'я повинно бути довшим за 5 символів", fg="red")

    input_field_user_name = Entry(rootWindow)  # Creates a text input field

    confirmation_button = Button(rootWindow, text="Підтвердити")
    pack_widgets(label_user_name, input_field_user_name, confirmation_button)


def pack_widgets(label_user_name, input_field_user_name, confirmation_button):
    label_user_name.grid(row=0)

    input_field_user_name.grid(row=2)

    confirmation_button.grid(row=3)

    rootWindow.mainloop()  # Infinite loop for UI


create_widgets()



