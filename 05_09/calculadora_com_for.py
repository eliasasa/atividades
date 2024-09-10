import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry('300x500')
app.configure(fg_color='#1E1E1E')
app.title('Calculadora')

app.columnconfigure(0, weight=1)
app.columnconfigure(3, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(5, weight=0)

but_cor = '#323232'
but_hov = '#4D4D4D' 
text_cor = '#FFFFFF'
but_red = '#ff99a1'
but_red_hov = '#e88c93'
but_numpad = '#3b3b3b'


<<<<<<< HEAD
resp_frm = ctk.CTkFrame(app, height=175, fg_color='#333333')
resp_frm.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=3, padx=2)
resp_frm.columnconfigure(0, weight=1)
resp_frm.rowconfigure(0, weight=1)

result_lbl = ctk.CTkLabel(resp_frm, text='0', font=('Segoe UI', 60), text_color='white')
result_lbl.grid(row=0, column=0, sticky='e', padx=(0, 5), pady=10)

def ajuste_font():
    x = result_lbl.cget('text')
    font_size = 60
    if len(x) > 8:
        font_size = max(30, 60 - (len(x) - 8) * 5)
    result_lbl.configure(font=('Segoe UI', font_size))
=======
resp_frm = ctk.CTkFrame(app, height=175, fg_color='#1E1E1E')
resp_frm.grid(row=0, column=0, columnspan=4, sticky='new', pady=0, padx=3)
>>>>>>> 181f8078237d7c563e28e9b784bf69a6a02f91ad

botoes = [
    ('%', 'CE', 'C', '⌫'),
    ('¹/ₓ', 'x²', '²√x', '÷'),
    ('7', '8', '9', 'x'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('+/-', '0', ',', '=')
]

botoes_dic = {}

def get_text(texto):
    x = result_lbl.cget('text')
    if x == '0' and texto.isdigit():
        result_lbl.configure(text=texto)
        ajuste_font()
    elif texto.isdigit() and len(x) < 18:
        result_lbl.configure(text=f'{x}{texto}')
        ajuste_font()
    elif texto == 'C':
        result_lbl.configure(text='0')
        ajuste_font()
    elif texto == '⌫':
        if len(x) > 1:
            new_text = x[:-1]
        else:
            new_text = '0'
        result_lbl.configure(text=new_text)
        ajuste_font()
    elif texto in ('%', 'CE', '1/x', 'x²', '²√x', '÷', 'x', '-', '+', '='):
        if x == '0' and texto in '+-*/':
            result_lbl.configure(text=texto)
        else:
            result_lbl.configure(text=f'{x}{texto}')
        ajuste_font()

    


row_index = 0
for row in botoes:
    column_index = 0
    for text in row:
        nome = f'{text}_but'
        botoes_dic[nome] = ctk.CTkButton(app, text=text, height=50, width=73, font=('Segoe UI', 20), fg_color=but_cor, hover_color=but_numpad, text_color=text_cor, command=lambda t=text: get_text(t)) 
        botoes_dic[nome].grid(row=row_index + 1, column=column_index, padx=1, pady=1, sticky='nsew')
        if text == '=':
            botoes_dic[nome].configure(fg_color=but_red, hover_color=but_red_hov)
        elif row_index >= 2 and column_index <= 2:
            botoes_dic[nome].configure(fg_color=but_numpad, hover_color=but_cor)   
        column_index += 1
    row_index += 1

app.mainloop()
