import tkinter as tk
from tkinter import ttk
from tkinter import *

# root window
root = Tk()
root.title('Syberia - Ajuda')
root.geometry('800x600')

nome = ""

# style
styl = ttk.Style()
styl.configure('blue.TSeparator', background='blue')
styl.configure('red.TSeparator', background='red')
styl.configure('blk.TSeparator', background='black')


def focus(e, nome):
    if nome == "lab1":
        lab1["foreground"] = "red"
    elif nome == "lab2":
        lab2["foreground"] = "red"
    elif nome == "lab3":
        lab3["foreground"] = "red"


def unfocus(e, nome):
    if nome == "lab1":
        lab1["foreground"] = "black"
    elif nome == "lab2":
        lab2["foreground"] = "black"
    elif nome == "lab3":
        lab3["foreground"] = "black"


lab1 = Label(root, text="Doenças", font="Helvetica 10 bold", justify="left", cursor="hand1", fg="black")
lab1.bind("<Enter>", lambda e: focus(e, "lab1"))
lab1.bind("<Leave>", lambda e: unfocus(e, "lab1"))

lab2 = Label(root, text="Medicamentos", font="Helvetica 10 bold", justify="left", cursor="hand1", fg="black")
lab2.bind("<Enter>", lambda e: focus(e, "lab2"))
lab2.bind("<Leave>", lambda e: unfocus(e, "lab2"))

lab3 = Label(root, text="Legendas", font="Helvetica 10 bold", justify="left", cursor="hand1", fg="black")
lab3.bind("<Enter>", lambda e: focus(e, "lab3"))
lab3.bind("<Leave>", lambda e: unfocus(e, "lab3"))

lab1.grid(row=0, column=0, padx=10, sticky=(E, W))
lab2.grid(row=0, column=1, padx=10, sticky=(E, W))
lab3.grid(row=0, column=2, padx=10, sticky=(E, W))

# horizontal separator
ttk.Separator(
    master=root,
    orient=HORIZONTAL,
    style='blk.TSeparator',
    class_=ttk.Separator,
    takefocus=1,
    cursor=''
).grid(row=2, column=0, ipadx=800, pady=0, columnspan=99, sticky=(W, E))

root.mainloop()
