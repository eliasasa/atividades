import tkinter as tk
from PIL import Image, ImageTk

def atualizar_imagem(indice):
    global img_tk
    image_path = imagens[indice]
    img = Image.open(image_path)
    img = img.resize((300, 300)) 
    img_tk = ImageTk.PhotoImage(img)
    label_imagem.config(image=img_tk)
    label_imagem.image = img_tk

def prox():
    global x
    x += 1
    if x >= len(imagens):
        x = 0
    atualizar_imagem(x)

def ant():
    global x
    x -= 1
    if x < 0:  
        x = len(imagens) - 1
    atualizar_imagem(x)


janela = tk.Tk()
janela.geometry('500x600')
janela.config(bg='#451952')

x = 0

imagens = [
    '22_08/bisnaga.webp',
    '22_08/cellbit.jpg',
    '22_08/image1.jfif',
    '22_08/Internet-O-Filme.jpg',
    '22_08/caveirao.jpg'
]

titulo = tk.Label(text='Galeria', font=('Arial', 36, 'bold'), bg='#451952', fg='white')
titulo.place(anchor='center', relx=0.5, rely=0.05)

bdire = tk.Button(text='   <   ', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=ant)
bdire.place(anchor='w', relx=0, rely=0.5)

besq = tk.Button(text='   >   ', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=prox)
besq.place(anchor='e', relx=1, rely=0.5)

img_tk = None
label_imagem = tk.Label(janela)
label_imagem.place(anchor='center', relx=0.5, rely=0.5)
atualizar_imagem(x)


ent1=tk.Entry(width=35, bg='#AE445A', fg='#451952', font=('Arial', 16))
ent1.place(anchor='center', rely=0.9, relx=0.5)
ent1.bind('<Return>', comentario)


janela.mainloop()
