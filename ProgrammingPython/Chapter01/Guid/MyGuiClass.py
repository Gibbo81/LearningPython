from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        button = Button(self, text='Press', command= self.ToReply)
        button.pack()
    
    def ToReply(self):
        showinfo(title='popup', message='Button Pressed')

class CustomGui(MyGui):
    def ToReply(self):
        showinfo(title='Bad', message='Why did you do it?!?!?')



if __name__=="__main__":
    window = MyGui()
    window.pack()
    window.mainloop()

    


