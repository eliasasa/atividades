import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry('300x500')
app.configure(fg_color='#1E1E1E')
app.title('Calculadora')

app.columnconfigure(0, weight=1)
app.columnconfigure(3, weight=1)

app.rowconfigure(0, weight=0)
app.rowconfigure(5, weight=0)

but_cor = '#333333'
but_hov = '#4D4D4D' 
text_cor = '#FFFFFF'

resp_frm = ctk.CTkFrame(app, height=175, fg_color='#333333')
resp_frm.grid(row=0, column=0, columnspan=4, sticky='new', pady=0, padx=3)

#isso é ridiculo wtf
botoes = [
    ('%', 'CE', 'C', '⌫'),
    ('1/x', 'x²', '²√x', '÷'),
    ('7', '8', '9', 'x'),
    ('4', '5', '6', '-'),
    ('1', '2', '3', '+'),
    ('+/-', '0', ',', '=')
]

botoes_dic={}

def get_text(texto):
    print(f'Texto do botão clicado: {texto}')

row_index = 0
for row in botoes:
    collumn_index = 0
    for text in row:
        nome = f'{text}_but'
        botoes_dic[nome]= ctk.CTkButton(app, text=text, height=50, width=70, font=('Segoe UI', 20), fg_color=but_cor, hover_color=but_hov, text_color=text_cor, command=lambda t=text: get_text(t))
        botoes_dic[nome].grid(row=row_index + 1, column=collumn_index, padx=2, pady=2, sticky='nsew')
        collumn_index += 1
    row_index += 1


app.mainloop()
