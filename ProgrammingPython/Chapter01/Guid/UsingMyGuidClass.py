from tkinter import *
from MyGuiClass import MyGui
from MyGuiClass import CustomGui
from tkinter.messagebox import showinfo

def Reply(name):
    showinfo(title='popup', message='Hello %s!' % name)

mainwindow = Tk()        #main application window
mainwindow.iconbitmap('symantec.ico')
Label(mainwindow, text =__name__).pack()

popout = Toplevel()     #we create two different widget
Label(popout, text = 'Attach').pack(side=LEFT)
MyGui(popout).pack(side=RIGHT)
CustomGui(popout).pack(side = TOP)

popouttwo = Toplevel() 
popouttwo.iconbitmap('python.ico')
Label(popouttwo, text = 'Insert Your Name').pack(side=TOP)
ent = Entry(popouttwo)
ent.pack(side=TOP)
Button(popouttwo, text='press', command = (lambda: Reply(ent.get()))).pack(side=TOP)

mainwindow.mainloop()


