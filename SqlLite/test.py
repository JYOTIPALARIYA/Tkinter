from tkinter import *
import time

top = Tk()
def Run(object):
    object.config(state = 'disabled')
    b1.update()
    time.sleep(5)
    object.config(state = 'normal')
    b1.update()

b1 = Button(top, text = 'RUN', command = lambda : Run(b1))
b1.pack()

top.mainloop()