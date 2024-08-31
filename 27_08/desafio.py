import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# Cria a janela principal
app = ctk.CTk()
app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}+0+0")


app.configure(fg_color='black')

imagem1_global = None
imagem3_global = None

def comparaçoes():
    x = usere1.get()
    y = senhere1.get()
    z = senhere2.get()

    if len(x) <= 0 or len(y) <= 0 or len(z) <= 0:
        alert1 = ctk.CTkLabel(app, text='Algum(s) dos campos está vazio', font=('Arial', 15, 'bold'), text_color='red')
        alert1.place(relx=0.807, rely=0.87, anchor='center')
        alert1.after(1000, alert1.destroy)

    elif x == y:
        alert2 = ctk.CTkLabel(app, text='Senha e nome de usuário não podem ser idênticos', font=('Arial', 15, 'bold'), text_color='red')
        alert2.place(relx=0.807, rely=0.87, anchor='center')
        alert2.after(1000, alert2.destroy)
    
    elif y != z:
        alert3 = ctk.CTkLabel(app, text='As senhas digitadas não coincidem', font=('Arial', 15, 'bold'), text_color='red')
        alert3.place(relx=0.807, rely=0.87, anchor='center')
        alert3.after(1000, alert3.destroy)

    else:
        abrir_nova_pagina()

def escondidinho():
    if senhere1.cget('show') == '*':
        senhere1.configure(show='')
        senhere2.configure(show='')
        show_but.configure(text='Ocultar senha', fg_color='#000000')
    else:
        senhere1.configure(show='*')
        senhere2.configure(show='*')
        show_but.configure(text='Mostrar senha', fg_color='#666666')

def limpar_tudo():
    for widget in app.winfo_children():
        widget.destroy()
    cardapio()

def abrir_nova_pagina():
    frame_cadastro.place_forget()
    nova_pagina = ctk.CTkFrame(app, width=600, height=600, corner_radius=10, fg_color='#333333')
    nova_pagina.place(relx=0.5, rely=0.5, anchor='center')
    titulo_pagina = ctk.CTkLabel(nova_pagina, text="Cadastro Concluído", font=('Century Gothic', 40, 'bold'), text_color='white')
    titulo_pagina.pack(padx=20, pady=(30, 20), anchor="n")
    mensagem = ctk.CTkLabel(nova_pagina, text="Seu cadastro foi concluído com sucesso!", font=('Century Gothic', 20), text_color='white')
    mensagem.pack(padx=20, pady=(10, 40), anchor="n")
    botao_voltar = ctk.CTkButton(nova_pagina, text="Fazer compras", command=limpar_tudo, font=('Century Gothic', 18, 'bold'), fg_color='#555555', text_color='white')
    botao_voltar.pack(padx=20, pady=20, anchor="s")

def cardapio():
    global imagem3_global
    
    image_path3 = '27_08/rr.jpg'
    image3 = Image.open(image_path3)
    image3 = ImageTk.PhotoImage(image3)
    imagem3_global = ctk.CTkLabel(app, image=image3, text='')
    imagem3_global.place(relx=0.5, rely=0.5, anchor='center')
    imagem3_global.image = image3

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)
    app.grid_columnconfigure(3, weight=1)
    app.grid_columnconfigure(4, weight=1)
    app.grid_columnconfigure(5, weight=1)
    app.grid_columnconfigure(6, weight=1)

    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)


    label1 = ctk.CTkLabel(app, image=tk_image2, text='')
    label1.grid(row=0, column=1, padx=50, pady=10)

    label2 = ctk.CTkLabel(app, image=tk_image2, text='')
    label2.grid(row=0, column=3, padx=10, pady=10)

    label3 = ctk.CTkLabel(app, image=tk_image2, text='')
    label3.grid(row=0, column=5, padx=10, pady=10)

    label4 = ctk.CTkLabel(app, image=tk_image2, text='')
    label4.grid(row=1, column=1, padx=10, pady=10)

    label5 = ctk.CTkLabel(app, image=tk_image2, text='')
    label5.grid(row=1, column=3, padx=10, pady=10)
    
    label6 = ctk.CTkLabel(app, image=tk_image2, text='')
    label6.grid(row=1, column=5, padx=10, pady=10)

titulo = ctk.CTkLabel(app, text="Le Gourmet d'Éderson", font=('Monotype Corsiva', 60), text_color='white', fg_color='black')
titulo.pack(padx=30, pady=(25, 0), anchor="w")

app.update_idletasks()

image_path2 = '27_08/Le Gourmet (1).png'
image2 = Image.open(image_path2)
titulo_height = titulo.winfo_height() 
image2 = image2.resize((int(180 * image2.width / image2.height), 180))
tk_image2 = ImageTk.PhotoImage(image2)

imagem2 = tk.Label(app, image=tk_image2, bg='black')
imagem2.place(relx=0.958, rely=0.0, anchor='ne')

# vinho
image_path = "27_08/vinho massa.jpg"
image = Image.open(image_path)
max_width = int(app.winfo_screenwidth() * 0.9)
max_height = int(app.winfo_screenheight() * 0.9)
image.thumbnail((max_width, max_height))

tk_image = ImageTk.PhotoImage(image)
imagem1_global = ctk.CTkLabel(app, image=tk_image, text='')
imagem1_global.pack(anchor="w", padx=0, pady=(50,0))

frame_cadastro = ctk.CTkFrame(app, width=600, height=600, corner_radius=10, fg_color='#333333')
frame_cadastro.place(relx=0.95, rely=0.3, anchor='ne')

titulo_frame = ctk.CTkLabel(frame_cadastro, text="Cadastro", font=('Century Gothic', 40, 'bold'), text_color='white')
titulo_frame.pack(padx=100, pady=(30, 20), anchor="n")

user1 = ctk.CTkLabel(frame_cadastro, text="Usuário:", font=('Century Gothic', 20), text_color='white')
user1.pack(padx=20, pady=(20,5), anchor="w")

usere1 = ctk.CTkEntry(frame_cadastro, width=350, fg_color='#555555', text_color='white')
usere1.pack(padx=20, pady=0, anchor='w')

senha1 = ctk.CTkLabel(frame_cadastro, text="Senha:", font=('Century Gothic', 20), text_color='white')
senha1.pack(padx=20, pady=(10,5), anchor="w")

senhere1 = ctk.CTkEntry(frame_cadastro, width=350, show='*', fg_color='#555555', text_color='white')
senhere1.pack(padx=20, pady=0, anchor='w')

senha2 = ctk.CTkLabel(frame_cadastro, text="Reescreva sua senha:", font=('Century Gothic', 20), text_color='white')
senha2.pack(padx=20, pady=(10,5), anchor="w")

senhere2 = ctk.CTkEntry(frame_cadastro, width=350, show='*', fg_color='#555555', text_color='white')
senhere2.pack(padx=20, pady=(0,40), anchor='w')

show_but = ctk.CTkButton(frame_cadastro, text='Mostrar senha', command=escondidinho, width=25, height=25, fg_color='#666666')
show_but.place(relx=0.947, rely=0.73, anchor='ne')

cad_but = ctk.CTkButton(frame_cadastro, width=40, height=40, text='Cadastrar', font=('Century Gothic', 24, 'bold'), command=comparaçoes, fg_color='#555555', text_color='white')
cad_but.pack(padx=0, pady=(10, 40))



app.mainloop()
