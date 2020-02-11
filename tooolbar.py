from tkinter import *

def printfile():
    print("File Printed")

def savefile():
    print("File Saved")


root = Tk()

toolbar = Frame(root,bg="Green")

printbtn = Button(toolbar, text="Insertfiles", padx=10, pady=10,bg="Red", command=printfile)
printbtn.pack(side=LEFT)

s = Button(toolbar, text="Save File", padx=10, pady=10, command=savefile)
s.pack(side=LEFT)

toolbar.pack(side=TOP, fill=X)

root.mainloop()