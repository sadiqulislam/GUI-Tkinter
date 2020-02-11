from tkinter import *

root = Tk()

frame1 = Frame(root)
frame1.pack()

frame2 = Frame(root)
frame2.pack(side=LEFT)

button1 = Button(frame1, text="Click Here", fg="Green")
button1.pack()

button2 = Button(frame2, text="Click", fg="Red")
button2.pack()

root.mainloop()
