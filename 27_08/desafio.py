import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}+0+0")
app.configure(fg_color='black')

imagem1_global = None
imagem3_global = None


jantares = {
    'Hot-Nana': 10,
    'Múmia mexicana': 40,
    'Fabio & Nuggets': 35,
    'Pseudo Sushi': 0.5,
    'Sobras do Pablo Marçal': 100,
    'Provavelmente comida': 25,
    'Leninade': 15,
    'Seda sabor Mel':11.5,
    'Qboa':20,
    'Coca-Cola sabor Ebola': 13.5,
    'Poção de Cura': 25,
    'Perfume Palmeiras - Jequiti':30,
    '7belo sabor Body Splash':20,
    'Dormec (pacote)':16.5,
    'KitKat frutos do mar':20,
    'Fatia bolo do Shrek':8.5,
    'Sorvete de lula':7,
    'Tandy diversos sabores':9.5
}

quantidade_global = {produto: 0 for produto in jantares}

carrinho = {}
total = 0

def total_car(frame):
    global carT
    carT = ctk.CTkLabel(frame, text=f'Total do carrinho:\nR${total}', font=('Monotype Corsiva', 30), text_color='white')
    carT.grid(row=0, column=2)


def add_car(produto, quantidade=1):
    global total, carrinho, quantidade_global  
    if produto in jantares:
        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade


        total = sum(carrinho[produto] * jantares[produto] for produto in carrinho)
        print(f"Carrinho: {carrinho}")
        print(f"Total: R$ {total:.2f}")

        quantidade_global[produto] = carrinho[produto]
        
        carT.configure(text=f'Total do carrinho:\nR${total}')


def comparaçoes():
    global x
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

def limpar_tudoE(event):
    for widget in app.winfo_children():
        widget.destroy()
    cardapio()

def limpar_cardapio(event):
    for widget in app.winfo_children():
        if widget != imagem3_global:
            widget.destroy()
    comidas()

def limpar_drinks(event):
    for widget in app.winfo_children():
        if widget != imagem3_global:
            widget.destroy()
    drinks()

def limpar_doces(event):
    for widget in app.winfo_children():
        if widget != imagem3_global:
            widget.destroy()
    doces()

def limpar_pag():
    for widget in app.winfo_children():
        if widget != imagem3_global:
            widget.destroy()
    pag()

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

def bt_buy(nmframe, produto):
    lb_qt = ctk.CTkLabel(nmframe, text=str(quantidade_global.get(produto, 0)), font=('Arial', 36, 'bold'), bg_color='gray', text_color='white', width=100, height=30)
    lb_qt.place(relx=0.5, rely=0.9, anchor='center')

    def add():
        nonlocal lb_qt
        quantidade = int(lb_qt.cget('text')) + 1
        lb_qt.configure(text=str(quantidade))
        add_car(produto, 1) 

    def remv():
        nonlocal lb_qt
        quantidade = int(lb_qt.cget('text'))
        if quantidade > 0:
            lb_qt.configure(text=str(quantidade - 1))
            add_car(produto, -1)

    add_but = ctk.CTkButton(nmframe, text='+', font=('Arial', 34, 'bold'), fg_color='#111111',width=50, height=48, command=add, text_color='white', corner_radius=0)
    add_but.place(relx=1, rely=0.9, anchor='e')
    
    rmv_but = ctk.CTkButton(nmframe, text='-', font=('Arial', 34, 'bold'), fg_color='#111111',width=50, height=48, command=remv, text_color='white', corner_radius=0)
    rmv_but.place(relx=0.0, rely=0.9, anchor='w')

def pag_rel():
    for widget in app.winfo_children():
        if widget != imagem3_global:
            widget.destroy()
    fpag = ctk.CTkFrame(app, width=400, height=400, corner_radius=10, fg_color='green')
    fpag.grid(column=1, row=1)

    checkimg = Image.open('27_08/icons/gg--check-o.png')
    checkimg = ImageTk.PhotoImage(checkimg)
    fplab= ctk.CTkLabel(fpag, image=checkimg, text='')
    fplab.pack(padx=20, pady=20)

    msgf= ctk.CTkLabel(fpag, text='Obrigado por comprar conosco!', font=('Arial', 24, 'bold'), text_color='white')
    msgf.pack(padx=20, pady=20)

    def fim():
        app.destroy()

    app.after(5000, fim)

def pag():
    fframe = ctk.CTkFrame(app, width=700, height=500, corner_radius=10, fg_color='gray')
    fframe.grid(row=1, column=1, padx=10, pady=10)

    flabel = ctk.CTkLabel(fframe, text='Finalizar pedido', font=('Arial', 45, 'bold'))
    flabel.pack(padx=300, pady=10, anchor='center')

    fprod = ctk.CTkLabel(fframe, text='Carrinho', font=('Arial', 24, 'bold'))
    fprod.pack(padx=10, pady=10, anchor='w')

    carrinho_frame = ctk.CTkFrame(fframe, fg_color='#111111')
    carrinho_frame.pack(padx=10, pady=10, fill='both', expand=True)

    total_label = ctk.CTkLabel(carrinho_frame, text='Produto', font=('Arial', 18, 'bold'), width=200, anchor='w')
    total_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    
    qtd_label = ctk.CTkLabel(carrinho_frame, text='Quantidade', font=('Arial', 18, 'bold'), width=100, anchor='w')
    qtd_label.grid(row=0, column=1, padx=5, pady=5, sticky='w')
    
    valor_label = ctk.CTkLabel(carrinho_frame, text='Valor', font=('Arial', 18, 'bold'), width=100, anchor='e')
    valor_label.grid(row=0, column=2, padx=5, pady=5, sticky='e')

    row = 1
    for produto, quantidade in carrinho.items():
        ctk.CTkLabel(carrinho_frame, text=produto, font=('Arial', 16), anchor='w').grid(row=row, column=0, padx=5, pady=5, sticky='w')
        ctk.CTkLabel(carrinho_frame, text=str(quantidade), font=('Arial', 16), anchor='w').grid(row=row, column=1, padx=5, pady=5, sticky='w')
        ctk.CTkLabel(carrinho_frame, text=f'R$ {quantidade * jantares[produto]:.2f}', font=('Arial', 16), anchor='e').grid(row=row, column=2, padx=5, pady=5, sticky='e')
        row += 1

    total_label = ctk.CTkLabel(fframe, text=f'Total: R$ {total:.2f}', font=('Arial', 24, 'bold'), fg_color='gray', text_color='white')
    total_label.pack(padx=10, pady=10)

    

    hello = ctk.CTkLabel(app, text='Voltar ', font=('Monotype Corsiva', 60), text_color='white')
    hello.place(relx=0.1, rely=0.04)
    backimg = Image.open('27_08/icons/back-10.png')
    backimg = backimg.resize((50, 50))
    backimg = ImageTk.PhotoImage(backimg)
    backl = ctk.CTkLabel(app, image=backimg, text='')
    backl.bind("<Button-1>", command=limpar_tudoE)
    backl.place(relx=0.05, rely=0.065)

    finalizarbt=ctk.CTkButton(app, text='Finalizar\npedido', font=('Arial', 24, 'bold'), fg_color='green', text_color='white', hover_color='#006400', corner_radius=20, command=pag_rel)
    finalizarbt.place(relx=0.85, rely=0.85)

def doces():
    hello = ctk.CTkLabel(app, text='Doces ', font=('Monotype Corsiva', 60), text_color='white')
    hello.place(relx=0.1, rely=0.04)

    total_car(app)

    backimg = Image.open('27_08/icons/back-10.png')
    backimg = backimg.resize((50, 50))
    backimg = ImageTk.PhotoImage(backimg)
    backl = ctk.CTkLabel(app, image=backimg, text='')
    backl.bind("<Button-1>", command=limpar_tudoE)
    backl.place(relx=0.05, rely=0.065)

    ctk.CTkLabel(app, text='7belo sabor Body Splash - R$ 20,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.167, rely=0.27, ancho='center')
    frame1 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame1.grid(row=1, column=0, padx=5, pady=(5,3)) 
    icon1 = Image.open('27_08/comidas/doces/7belo.png')
    icon1 = ImageTk.PhotoImage(icon1)
    iconl = ctk.CTkLabel(frame1, image=icon1, text='')
    iconl.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame1, '7belo sabor Body Splash')
    
    ctk.CTkLabel(app, text='Dormec (pacote) - R$16,50', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.5, rely=0.27, ancho='center')
    frame2 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame2.grid(row=1, column=1, padx=5, pady=5)
    icon2 = Image.open('27_08/comidas/doces/dormec.jpg')
    icon2 = ImageTk.PhotoImage(icon2)
    iconl2 = ctk.CTkLabel(frame2, image=icon2, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame2, 'Dormec (pacote)')

    ctk.CTkLabel(app, text='KitKat frutos do mar - R$20,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.83, rely=0.27, ancho='center')
    frame3 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame3.grid(row=1, column=2, padx=5, pady=(3,5))
    icon3 = Image.open('27_08/comidas/doces/kitkat.jpg')
    icon3 = ImageTk.PhotoImage(icon3)
    iconl2 = ctk.CTkLabel(frame3, image=icon3, text='', font=('Arial', 25, 'bold'), text_color='black')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame3, 'KitKat frutos do mar')

    ctk.CTkLabel(app, text='Fatia Bolo Shrek - R$ 8,50', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.167, rely=0.66, ancho='center')
    frame4 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame4.grid(row=2, column=0, padx=5, pady=1)
    icon4 = Image.open('27_08/comidas/doces/shrek.jpg')
    icon4 = ImageTk.PhotoImage(icon4)
    iconl2 = ctk.CTkLabel(frame4, image=icon4, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame4, 'Fatia bolo do Shrek')

    ctk.CTkLabel(app, text='Sorvete de Lula - R$7,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.5, rely=0.66, ancho='center')
    frame5 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame5.grid(row=2, column=1, padx=5, pady=1)
    icon5 = Image.open('27_08/comidas/doces/sorvete.jpg')
    icon5 = ImageTk.PhotoImage(icon5)
    iconl2 = ctk.CTkLabel(frame5, image=icon5, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame5, 'Sorvete de lula')

    ctk.CTkLabel(app, text='Tandy diversos sabores - R9,50', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.83, rely=0.66, ancho='center')
    frame6 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame6.grid(row=2, column=2, padx=5, pady=1)
    icon6 = Image.open('27_08/comidas/doces/tendy.png')
    icon6 = ImageTk.PhotoImage(icon6)
    iconl2 = ctk.CTkLabel(frame6, image=icon6, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame6, 'Tandy diversos sabores')

def drinks():
    hello = ctk.CTkLabel(app, text='Drinks ', font=('Monotype Corsiva', 60), text_color='white')
    hello.place(relx=0.1, rely=0.04)

    total_car(app)

    backimg = Image.open('27_08/icons/back-10.png')
    backimg = backimg.resize((50, 50))
    backimg = ImageTk.PhotoImage(backimg)
    backl = ctk.CTkLabel(app, image=backimg, text='')
    backl.bind("<Button-1>", command=limpar_tudoE)
    backl.place(relx=0.05, rely=0.065)

    ctk.CTkLabel(app, text='Leninade ☭ - R$ 15,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.167, rely=0.27, ancho='center')
    frame1 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame1.grid(row=1, column=0, padx=5, pady=(5,3)) 
    icon1 = Image.open('27_08/comidas/drinks/limonada.jpg')
    icon1 = ImageTk.PhotoImage(icon1)
    iconl = ctk.CTkLabel(frame1, image=icon1, text='')
    iconl.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame1, 'Leninade')

    ctk.CTkLabel(app, text='Seda sabor Mel - R$11,50', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.5, rely=0.27, ancho='center')
    frame2 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame2.grid(row=1, column=1, padx=5, pady=5)
    icon2 = Image.open('27_08/comidas/drinks/mel.png')
    icon2 = ImageTk.PhotoImage(icon2)
    iconl2 = ctk.CTkLabel(frame2, image=icon2, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame2, 'Seda sabor Mel')

    ctk.CTkLabel(app, text='Qboa - R$20,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.83, rely=0.27, ancho='center')
    frame3 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame3.grid(row=1, column=2, padx=5, pady=(3,5))
    icon3 = Image.open('27_08/comidas/drinks/qboa.png')
    icon3 = ImageTk.PhotoImage(icon3)
    iconl2 = ctk.CTkLabel(frame3, image=icon3, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame3, 'Qboa')

    ctk.CTkLabel(app, text='Coca-Cola sabor Ebola - R$13,50', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.167, rely=0.66, ancho='center')
    frame4 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame4.grid(row=2, column=0, padx=5, pady=1)
    icon4 = Image.open('27_08/comidas/drinks/coca.jpg')
    icon4 = ImageTk.PhotoImage(icon4)
    iconl2 = ctk.CTkLabel(frame4, image=icon4, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame4, 'Coca-Cola sabor Ebola')

    ctk.CTkLabel(app, text='Poção de Cura - R$25,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.5, rely=0.66, ancho='center')
    frame5 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame5.grid(row=2, column=1, padx=5, pady=1)
    icon5 = Image.open('27_08/comidas/drinks/pocao.png')
    icon5 = ImageTk.PhotoImage(icon5)
    iconl2 = ctk.CTkLabel(frame5, image=icon5, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame5, 'Poção de Cura')

    ctk.CTkLabel(app, text='Perfume Jequiti sabor Palmeiras - R$30,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.83, rely=0.66, ancho='center')
    frame6 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame6.grid(row=2, column=2, padx=5, pady=1)
    icon6 = Image.open('27_08/comidas/drinks/perfume.png')
    icon6 = ImageTk.PhotoImage(icon6)
    iconl2 = ctk.CTkLabel(frame6, image=icon6, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame6, 'Perfume Palmeiras - Jequiti')

def comidas():
    hello = ctk.CTkLabel(app, text='Jantares ', font=('Monotype Corsiva', 60), text_color='white')
    hello.place(relx=0.1, rely=0.04)

    total_car(app)

    backimg = Image.open('27_08/icons/back-10.png')
    backimg = backimg.resize((50, 50))
    backimg = ImageTk.PhotoImage(backimg)
    backl = ctk.CTkLabel(app, image=backimg, text='')
    backl.bind("<Button-1>", command=limpar_tudoE)
    backl.place(relx=0.05, rely=0.065)

    ctk.CTkLabel(app, text='Hot-Nana - R$ 10,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.167, rely=0.27, ancho='center')
    frame1 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame1.grid(row=1, column=0, padx=5, pady=(5,3)) 
    icon1 = Image.open('27_08/comidas/janta/banana.jpg')
    icon1 = ImageTk.PhotoImage(icon1)
    iconl = ctk.CTkLabel(frame1, image=icon1, text='')
    iconl.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame1, 'Hot-Nana')

    ctk.CTkLabel(app, text='Múmia mexicana - R$ 40,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.5, rely=0.27, ancho='center')
    frame2 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame2.grid(row=1, column=1, padx=5, pady=5)
    icon2 = Image.open('27_08/comidas/janta/mumia.jpg')
    icon2 = ImageTk.PhotoImage(icon2)
    iconl2 = ctk.CTkLabel(frame2, image=icon2, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame2, 'Múmia mexicana')

    ctk.CTkLabel(app, text='Fabio & Nuggets - R$ 35,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.83, rely=0.27, ancho='center')
    frame3 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame3.grid(row=1, column=2, padx=5, pady=(3,5))
    icon3 = Image.open('27_08/comidas/janta/fred.png')
    icon3 = ImageTk.PhotoImage(icon3)
    iconl2 = ctk.CTkLabel(frame3, image=icon3, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame3, 'Fabio & Nuggets')

    ctk.CTkLabel(app, text='Pseudo Sushi - R$0,50', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.167, rely=0.66, ancho='center')
    frame4 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame4.grid(row=2, column=0, padx=5, pady=1)
    icon4 = Image.open('27_08/comidas/janta/sushi.jpg')
    icon4 = ImageTk.PhotoImage(icon4)
    iconl2 = ctk.CTkLabel(frame4, image=icon4, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame4, 'Pseudo Sushi')

    ctk.CTkLabel(app, text='Sobras do Pablo Marçal - R$100,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.5, rely=0.66, ancho='center')
    frame5 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame5.grid(row=2, column=1, padx=5, pady=1)
    icon5 = Image.open('27_08/comidas/janta/sobras.jpg')
    icon5 = ImageTk.PhotoImage(icon5)
    iconl2 = ctk.CTkLabel(frame5, image=icon5, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame5, 'Sobras do Pablo Marçal')

    ctk.CTkLabel(app, text='Provavelmente comida - R$25,00', font=('Arial', 25, 'bold'), text_color='white').place(relx=0.83, rely=0.66, ancho='center')
    frame6 = ctk.CTkFrame(app, width=350, height=245, corner_radius=10, fg_color='gray')
    frame6.grid(row=2, column=2, padx=5, pady=1)
    icon6 = Image.open('27_08/comidas/janta/boa.jpg')
    icon6 = ImageTk.PhotoImage(icon6)
    iconl2 = ctk.CTkLabel(frame6, image=icon6, text='')
    iconl2.place(relx=0.5, rely=0.4, anchor='center')
    bt_buy(frame6, 'Provavelmente comida')

def cardapio():
    global imagem3_global

    image_path3 = '27_08/fundo.jpg'
    image3 = Image.open(image_path3)
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    max_width = int(screen_width)
    max_height = int(screen_height)
    
    image3.thumbnail((max_width, max_height))
    image3_tk = ImageTk.PhotoImage(image3)
    
    imagem3_global = ctk.CTkLabel(app, image=image3_tk, text='')
    imagem3_global.place(relx=0.5, rely=0.5, anchor='center')
    imagem3_global.image = image3_tk

    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure(2, weight=1)

    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)


    hello = ctk.CTkLabel(app, text=f'Olá {x} ', font=('Monotype Corsiva', 60), text_color='white')
    hello.place(relx=0.04, rely=0.04)

    total_car(app)

    frame1 = ctk.CTkFrame(app, width=350, height=250, corner_radius=10, fg_color='gray')
    frame1.grid(row=1, column=0, padx=5, pady=(5,3)) 
    icon1 = Image.open('27_08/icons/comida2.png')
    icon1 = ImageTk.PhotoImage(icon1)
    iconl = ctk.CTkLabel(frame1, image=icon1, text='JANTARES', font=('Arial', 45, 'bold'))
    iconl.place(relx=0.5, rely=0.5, anchor='center')
    iconl.bind("<Button-1>", limpar_cardapio)

    frame2 = ctk.CTkFrame(app, width=350, height=250, corner_radius=10, fg_color='gray')
    frame2.grid(row=1, column=1, padx=5, pady=5)
    icon2 = Image.open('27_08/icons/hugeicons--drink.png')
    icon2 = ImageTk.PhotoImage(icon2)
    iconl2 = ctk.CTkLabel(frame2, image=icon2, text='DRINKS', font=('Arial', 45, 'bold'))
    iconl2.place(relx=0.5, rely=0.5, anchor='center')
    iconl2.bind("<Button-1>", limpar_drinks)

    frame3 = ctk.CTkFrame(app, width=350, height=250, corner_radius=10, fg_color='gray')
    frame3.grid(row=1, column=2, padx=5, pady=(3,5))
    icon3 = Image.open('27_08/icons/mdi--candy.png')
    icon3 = ImageTk.PhotoImage(icon3)
    iconl2 = ctk.CTkLabel(frame3, image=icon3, text='DOCES', font=('Arial', 45, 'bold'))
    iconl2.place(relx=0.5, rely=0.5, anchor='center')
    iconl2.bind("<Button-1>", limpar_doces)

    bt_fim = ctk.CTkButton(app, text=' Finalizar pedido ', fg_color='green', text_color='white', font=('Arial', 40, 'bold'), hover_color='#006400', corner_radius=20, command=limpar_pag)
    bt_fim.grid(row=2, column=2)

titulo = ctk.CTkLabel(app, text="Le Gourmet d'Éderson ", font=('Monotype Corsiva', 60), text_color='white', fg_color='black')
titulo.pack(padx=30, pady=(25, 0), anchor="w")

app.update_idletasks()

image_path2 = '27_08/Le Gourmet (1).png'
image2 = Image.open(image_path2)
titulo_height = titulo.winfo_height() 
image2 = image2.resize((int(180 * image2.width / image2.height), 180))
tk_image2 = ImageTk.PhotoImage(image2)

imagem2 = tk.Label(app, image=tk_image2, bg='black')
imagem2.place(relx=0.958, rely=0.0, anchor='ne')

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