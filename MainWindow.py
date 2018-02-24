from tkinter import *  # Import all packages from tkinter

rootWindow = Tk()  # Creates a blank window

topFrame = Frame(rootWindow)  # Basic layout that goes to the main root window
topFrame.pack()

bottomFrame = Frame(rootWindow)
bottomFrame.pack(side=BOTTOM)

submitButton = Button(bottomFrame, text="Прийняти", fg="green")  # Creates a red button with Submit text
declineButton = Button(bottomFrame, text="Відмінити", fg="red")  # Blue button

startButton = Button(topFrame, text="Розпочати", fg="blue")

declineButton.pack(side=LEFT)
submitButton.pack(side=LEFT)

startButton.pack()

rootWindow.mainloop()  # Infinite loop for UI
