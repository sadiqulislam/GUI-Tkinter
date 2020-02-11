from tkinter import *


def openproject():
    print("Welcome To New Project")


def save():
    print("Successfully Saved")


root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open Project", command=openproject)
submenu.add_command(label="Save", command=save)
root.mainloop()
