from tkinter import *

root = Tk()

def click():
    print("You Clicked Here")


button1 = Button(root,text="Click Here",command=click)
button1.pack()
root.mainloop()