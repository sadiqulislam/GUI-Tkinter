from tkinter import *

root = Tk()

label1 = Label(root, text="First Name", bg="Red", fg="Green")
label2 = Label(root, text="Last Name", bg="Red", fg="Green")

label1.pack(fill=X)
label2.pack(side=LEFT, fill=Y)

root.mainloop()