import tkinter as tk
import json
import os
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

# root window
root = Tk()
root.title('Syberia - Ajuda')
root.geometry('800x600')

nome = ""
global mystringvar
mystringvar = ""


# funcoes
def medicamentos_class(event, *args):
    for widget in frame2.winfo_children():
        widget.destroy()

    indice = event.widget.current()
    enfermidades = json_files[indice]

    print(indice)
    print(enfermidades)

    Label(frame2, text=enfermidades.upper(), font='Helvetica 18 bold').grid(stick="E", row=0, column=0)
    fileobject = open('dados/' + enfermidades + '.json', 'r')
    json_data = fileobject.read()
    data = json.loads(json_data)
    j = 0
    k = 0
    r = 2
    # cabecalho = ['Substance', 'Level', 'Container', 'Heal Time (s)', 'Overdose Increment']

    cabecalho = data[0].keys()

    for titulo in cabecalho:
        b = Label(frame2, text=titulo, relief=SOLID, width=16, borderwidth=1, bg="LightGrey")
        b.grid(sticky="W", row=1, column=j)
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
frame1 = ttk.Frame(root, borderwidth=0, width=0, height=110, relief=SOLID)
frame1['padding'] = (10, 10, 0, 10)
frame2 = ttk.Frame(root, borderwidth=0, width=0, height=0, relief=SOLID)
frame2['padding'] = (15, 15, 15, 15)

json_files = list((os.path.splitext(f)[0] for f in os.listdir("dados") if f.endswith('.json')))
json_text = list(
    os.path.splitext(f)[0].replace('_', ' ').capitalize() for f in os.listdir("dados") if f.endswith('.json'))
print(json_files)
print(json_text)

i=0;
for enfermidade in json_files:
    caminho = "imagens/" + enfermidade + ".png"
    print (str(i) + " " + caminho)
    root.photo = PhotoImage(file=caminho)
    Button(frame1, image=root.photo).grid(row=0, column=i)
    i += 1


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

# Create an object of tkinter ImageTk
imagem = Image.open("imagens/legendas.png")
imagem = imagem.resize((640, 480))
imagem = ImageTk.PhotoImage(imagem)
#

root.mainloop()
