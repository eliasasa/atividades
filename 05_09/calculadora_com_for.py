import customtkinter as ctk

app = ctk.CTk()
app.geometry('300x500')
app.configure(fg_color='#1E1E1E')
app.title('Calculadora')

app.columnconfigure(0, weight=1)
app.columnconfigure(3, weight=1)

app.rowconfigure(0, weight=0)
app.rowconfigure(0, weight=1)
app.rowconfigure(5, weight=0)

but_cor = '#333333'
but_cor = '#323232'
but_hov = '#4D4D4D' 
text_cor = '#FFFFFF'
but_red = '#ff99a1'
but_red_hov = '#e88c93'
but_numpad = '#3b3b3b'

resp_frm = ctk.CTkFrame(app, height=175, fg_color='#1E1E1E')
resp_frm.grid(row=0, column=0, columnspan=4, sticky='new', pady=0, padx=3)
resp_frm.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=3, padx=2)
resp_frm.columnconfigure(0, weight=1)
resp_frm.rowconfigure(0, weight=1)
resp_frm.rowconfigure(2, weight=1)

hist_result = ctk.CTkLabel(resp_frm, text='', font=('Segoe UI', 20), text_color='#5b5b5b')
hist_result.grid(row=0,column=0, sticky='e', padx=(0,5))

result_lbl = ctk.CTkLabel(resp_frm, text='0', font=('Segoe UI', 60), text_color='white')
result_lbl.grid(row=1, column=0, sticky='e', padx=(0, 5), pady=10)

def ajuste_font():
    x = result_lbl.cget('text')
    font_size = 60
    if len(x) > 8:
        font_size = max(30, 60 - (len(x) - 8) * 5)
    result_lbl.configure(font=('Segoe UI', font_size))

botoes = [
    ('%', 'CE', 'C', '⌫'),
    ('1/x', 'x²', '²√x', '÷'),
    ('7', '8', '9', 'x'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('+/-', '0', ',', '=')
]

botoes_dic={}
botoes_dic = {}

global cont, somes, sub, mult, div
cont = 0
somes = False
sub = False
mult = False
div = False

def get_text(texto):
    x = result_lbl.cget('text') 
    y = hist_result.cget('text')

    if x == '0' and texto.isdigit() or x == 'Erro':
        result_lbl.configure(text=texto)
    elif texto.isdigit() and len(x) < 18:
        result_lbl.configure(text=f'{x}{texto}')
    elif texto == 'C':
        result_lbl.configure(text='0')
        global cont
        cont = 0
    elif texto == 'CE':
        result_lbl.configure(text='0')
        hist_result.configure(text='')
    elif texto == '⌫':
        if len(x) > 1:
            new_text = x[:-1]
            if ',' not in new_text:
                cont = 0
        else:
            new_text = '0'
            cont = 0 
        result_lbl.configure(text=new_text)
    elif texto == ',' and cont < 1:
        result_lbl.configure(text=f'{x},')
        cont += 1
    elif texto == '%':
        x = float(x) / 100
        x = str(x)
        x = x.replace('.', ',')
        result_lbl.configure(text=f'{x}')
        cont += 1
    elif texto == '+/-':
        if ',' in x or '.' in x:
            x = x.replace(',', '.')
            x = float(x) * -1
            x = str(x)
            x = x.replace('.', ',')
        else: 
            x = int(x) * -1
        result_lbl.configure(text=f'{x}')
    elif texto == 'x²':
        if ',' in x or '.' in x:
            x = x.replace(',', '.')
            x = float(x) ** 2
            x = str(x)
            x = x.replace('.', ',')
        else:
            x = int(x) ** 2
            x = str(x)
            x = x.replace('.', ',')
        result_lbl.configure(text=f'{x}')
    elif texto == '²√x':
        if ',' in x or '.' in x:
            x = x.replace(',', '.')
            x = float(x) ** (1/2)
            x = str(x)
            x = str(x.replace('.', ','))
        else: 
            x = int(x) ** (1/2)
            x = str(x)
            x = str(x.replace('.', ','))
        result_lbl.configure(text=f'{x}')
    elif texto == '1/x':
        if ',' in x or '.' in x:
            x = x.replace(',', '.')
            x = 1 / float(x)
            x = str(x)
            x = str(x.replace('.', ','))
        else: 
            x = 1 / int(x)
            x = str(x)
            x = str(x.replace('.', ','))
        result_lbl.configure(text=f'{x}')
    elif texto in '+-x/÷':
        hist_result.configure(text=x)
        result_lbl.configure(text='0')
        cont = 0
        if texto == '+':
            global somes
            somes = True
        elif texto == '-':
            global sub
            sub = True
        elif texto == 'x':
            global mult
            mult = True
        elif texto == '÷':
            global div
            div = True
    elif texto == '=':
        try:
            x = float(x.replace(',', '.'))
            y = float(y.replace(',', '.'))
            if somes == True:
                somes = False
                total = y + x
            elif sub == True:
                sub = False
                total = y - x
            elif mult == True:
                mult = False
                total = y * x
            elif div == True:
                div = False
                try:
                    total = y / x
                except ZeroDivisionError:
                    total = 'Erro'
            total = str(total)
            total = str(total.replace('.', ','))
            result_lbl.configure(text=f'{total}')
            hist_result.configure(text='')
        except ValueError:
            result_lbl.configure(text='Erro')
    ajuste_font()

row_index = 0
for row in botoes:
    collumn_index = 0
    column_index = 0
    for text in row:
        global t
        nome = f'{text}_but'
        botoes_dic[nome]= ctk.CTkButton(app, text=text, height=50, width=70, font=('Segoe UI', 20), fg_color=but_cor, hover_color=but_hov, text_color=text_cor, command=lambda t=text: get_text(t))
        botoes_dic[nome].grid(row=row_index + 1, column=collumn_index, padx=2, pady=2, sticky='nsew')
        collumn_index += 1
        botoes_dic[nome] = ctk.CTkButton(app, text=text, height=50, width=73, font=('Segoe UI', 20), fg_color=but_cor, hover_color=but_numpad, text_color=text_cor, command=lambda t=text: get_text(t)) 
        botoes_dic[nome].grid(row=row_index + 1, column=column_index, padx=1, pady=1, sticky='nsew')
        if text == '=':
            botoes_dic[nome].configure(fg_color=but_red, hover_color=but_red_hov)
        elif row_index >= 2 and column_index <= 2:
            botoes_dic[nome].configure(fg_color=but_numpad, hover_color=but_cor)   
        column_index += 1
    row_index += 1

app.mainloop()