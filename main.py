import tkinter as tk
import json
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

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


# funcoes
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


def doencas_class(event):
    for widget in frame2.winfo_children():
        widget.destroy()

    ldoencas = ttk.Combobox(frame2, text="doencas")
    ldoencas['values'] = [0, 1, 2, 3, 4, 5, 6, 7]
    ldoencas.pack()


def medicamentos_class(event):
    for widget in frame2.winfo_children():
        widget.destroy()


    fileobject = open('dados/gripe.json', 'r')
    json_data = fileobject.read()
    data = json.loads(json_data)
    j = 0
    k = 0
    r = 1
   # cabecalho = ['Substance', 'Level', 'Container', 'Heal Time (s)', 'Overdose Increment']

    cabecalho = data[0].keys()

    for titulo in cabecalho:
        b = Label(frame2, text=titulo, relief=SOLID, width=16, borderwidth=1, bg="LightGrey" )
        b.grid(sticky="W", row=0, column=j)
        j = j + 1

    for linha in data:
        for titulo in cabecalho:
             b = Label(frame2, text=linha[titulo], relief=SOLID, width=16, borderwidth=1)
             b.grid(sticky="W", row=r, column=k)
             k = k + 1
        k = 0
        r = r + 1

def legendas_class(event):
    for widget in frame2.winfo_children():
        widget.destroy()

    llegendas = Label(frame2, image=imagem)
    llegendas.pack()


# widgets
frame1 = Frame(root, borderwidth=0, width=0, height=100, relief=SOLID)
frame2 = ttk.Frame(root, borderwidth=0, width=0, height=0, relief=SOLID)
frame2['padding'] = (15,15,15,15)


# frame3 = Frame(root, bg='#FF0000', borderwidth=1, width=0, height=50, relief=SOLID)

lab1 = Label(frame1, text="Doenças", font="Helvetica 10 bold", justify="left", cursor="hand1", fg="black", padx=10,
             pady=10)
lab1.bind("<Enter>", lambda e: focus(e, "lab1"))
lab1.bind("<Leave>", lambda e: unfocus(e, "lab1"))

lab2 = Label(frame1, text="Medicamentos", font="Helvetica 10 bold", justify="left", cursor="hand1", fg="black", padx=10,
             pady=10)
lab2.bind("<Enter>", lambda e: focus(e, "lab2"))
lab2.bind("<Leave>", lambda e: unfocus(e, "lab2"))

lab3 = Label(frame1, text="Legendas", font="Helvetica 10 bold", justify="left", cursor="hand1", fg="black", padx=10,
             pady=10)
lab3.bind("<Enter>", lambda e: focus(e, "lab3"))
lab3.bind("<Leave>", lambda e: unfocus(e, "lab3"))

lab_a = lab1.pack(side=LEFT)
lab_b = lab2.pack(side=LEFT)
lab_c = lab3.pack(side=LEFT)

# horizontal separator
separador_a = ttk.Separator(
    master=frame1,
    orient=HORIZONTAL,
    style='blk.TSeparator',
    class_=ttk.Separator,
    takefocus=1,
    cursor=''
).pack

frame1.pack(side="top", fill="x")
frame2.pack(expand=TRUE, fill=BOTH, )

# frame3.pack(side="bottom", fill="x")

# binds
lab1.bind("<Button-1>", doencas_class)
lab2.bind("<Button-1>", medicamentos_class)
lab3.bind("<Button-1>", legendas_class)

# Create an object of tkinter ImageTk
imagem = Image.open("imagens/legendas.png")
imagem = imagem.resize((640, 480))
imagem = ImageTk.PhotoImage(imagem)
#

root.mainloop()
