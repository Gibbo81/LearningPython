from tkinter import *
from tkinter.messagebox import showinfo

def Reply():
    showinfo(title='popup', message='Button Pressed')

window= Tk()        #main application window
button = Button(window, text='press', command=Reply)    #container are passed as the first argument
button.pack()
window.mainloop()

