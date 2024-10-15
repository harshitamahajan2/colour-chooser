from tkinter import *
from tkinter import colorchooser
root=Tk()
root.geometry('500x500')
root.config(bg='white')
def f1():
    res=colorchooser.askcolor(title=' select color')
    print(res)
    root.config(bg=res[1])
Button(root,text='select color', command=f1).pack()
root.mainloop()
