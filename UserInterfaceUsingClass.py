from tkinter import *

class MyButton:
    def __init__(self, root1):

        frame = Frame(root1)
        frame.pack()

        self.printbtn = Button(frame, text="Click", command=self.printmsg)
        self.printbtn.pack()

        self.quitbtn = Button(frame, text="Exit", command=frame.quit)
        self.quitbtn.pack()

    def printmsg(self):
        print("Welcome")

root = Tk()

s = MyButton(root)

root.mainloop()