import tkinter as tk
import json
import os
import time
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

# root window
root = Tk()
root.title('Syberia - Ajuda')
root.geometry('800x600')
root.configure(border=TRUE, borderwidth=2)
nome = ""
global mystringvar
mystringvar = ""

# # Setting icon of master window
p1 = PhotoImage(file='imagens\\favicon.png')
root.iconphoto(False, p1)

# funcoes
def medicamentos_class(*args):
    print(sb_ver.winfo_exists())

    for widget in frame2.winfo_children():
        # if not sb_ver.winfo_exists():
           widget.destroy()

    enfermidades = args[0]

    Label(frame2, text=enfermidades.upper(), font='Helvetica 18 bold').grid(stick="E", row=0, column=0)
    fileobject = open('dados/' + enfermidades + '.json', 'r')
    json_data = fileobject.read()
    data = json.loads(json_data)
    j = 0
    k = 0
    r = 2

    cabecalho = data[0].keys()

    for titulo in cabecalho:
        b = Label(frame2, text=titulo, relief=SOLID, width=16, borderwidth=1, bg="LightGrey")
        b.grid(sticky="EW", row=1, column=j)
        j = j + 1

    for linha in data:
        for titulo in cabecalho:
            b = Label(frame2, text=linha[titulo], relief=SOLID, width=16, borderwidth=1)
            b.grid(sticky="EW", row=r, column=k)
            k = k + 1
        k = 0
        r = r + 1

# widgets
frame1 = ttk.Frame(root, borderwidth=0, width=0, height=110, relief=SOLID)
frame1['padding'] = (1, 1, 1, 1)
frame2 = ttk.Frame(root, borderwidth=0, width=0, height=0, relief=SOLID)
frame2['padding'] = (15, 15, 15, 15)

sb_ver = Scrollbar(frame2, orient=VERTICAL)

json_files = list((os.path.splitext(f)[0] for f in os.listdir("dados") if f.endswith('.json')))
json_text = list(
    os.path.splitext(f)[0].replace('_', ' ').capitalize() for f in os.listdir("dados") if f.endswith('.json'))

i = 0;
root.tk_images = []

for enfermidade in json_files:
    caminho = "imagens/" + enfermidade + ".png"
    photo = PhotoImage(file=caminho)
    root.tk_images.append(photo)

    for imagem_botao in root.tk_images:
        btn = Button(frame1, image=imagem_botao, command=lambda m=json_files[i]: medicamentos_class(m))
        btn.grid(row=0, column=i)

    i += 1

frame1.pack(side="top", fill="x")
frame2.pack(expand=TRUE, fill=BOTH)


root.mainloop()
