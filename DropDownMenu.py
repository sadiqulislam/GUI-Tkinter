from tkinter import *


def openproject():
    print("Welcome To New Project")


def save():
    print("Successfully Saved")

def undo():
    print("Successfully Undo")

def redo():
    print("Successfully Redo")


root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open Project", command=openproject)
submenu.add_command(label="Save", command=save)

# Separator

submenu.add_separator()
submenu.add_command(label="Settings", command=openproject)
submenu.add_command(label="General", command=save)

# Edit Menu

editmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo",command=undo)
editmenu.add_command(label="Redo",command=redo)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo",command=undo)
newmenu.add_command(label="Redo",command=redo)


root.mainloop()
