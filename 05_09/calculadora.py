import customtkinter as ctk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry('300x500')
app.configure(fg_color='#1E1E1E')
app.title('Calculadora')

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)
app.columnconfigure(3, weight=1)

app.rowconfigure(0, weight=0)
app.rowconfigure(1, weight=0)
app.rowconfigure(2, weight=0)
app.rowconfigure(3, weight=0)
app.rowconfigure(4, weight=0)
app.rowconfigure(5, weight=0)

but_cor = '#333333'
but_hov = '#4D4D4D' 
text_cor = '#FFFFFF'

resp_frm = ctk.CTkFrame(app, height=175, fg_color='#333333')
resp_frm.grid(row=0, column=0, columnspan=4, sticky='new', pady=0, padx=3)

def but_padrao(nome, texto, linha, coluna):
    nome = ctk.CTkButton(app, text=texto, height=50, width=95, font=('Segoe UI', 24), fg_color=but_cor, hover_color=but_hov, text_color=text_cor)
    nome.grid(row=linha, column=coluna, padx=2, pady=2, sticky='new')

but_padrao('porc_but', '%', 1, 0)
but_padrao('ce_but', 'CE', 1, 1)
but_padrao('c_but', 'C', 1, 2)
but_padrao('apagar_but', '⌫', 1, 3)

but_padrao('1_by_x_but', '1/x', 2, 0)
but_padrao('quadrado_but', 'x²', 2, 1)
but_padrao('raiz_but', '²√x', 2, 2)
but_padrao('div_but', '÷', 2, 3)

but_padrao('7_but', '7', 3, 0)
but_padrao('8_but', '8', 3, 1)
but_padrao('9_but', '9', 3, 2)
but_padrao('mult_but', 'X', 3, 3)

but_padrao('4_but', '4', 4, 0)
but_padrao('5_but', '5', 4, 1)
but_padrao('6_but', '6', 4, 2)
but_padrao('sub_but', '-', 4, 3)

but_padrao('1_but', '1', 5, 0)
but_padrao('2_but', '2', 5, 1)
but_padrao('3_but', '3', 5, 2)
but_padrao('soma_but', '+', 5, 3)

but_padrao('inv_but', '+/-', 6, 0)
but_padrao('0_but', '0', 6, 1)
but_padrao('vrg_but', ',', 6, 2)
but_padrao('result_but', '=', 6, 3)

app.mainloop()
