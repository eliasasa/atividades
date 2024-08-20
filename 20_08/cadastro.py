import tkinter as tk
from tkinter import ttk

def mostrar_entrada(widget):
    texto = widget.get() 
    print(f"Texto digitado: {texto}")

def prox(event=None):
    widget_atual = event.widget

    mostrar_entrada(widget_atual)
    

    proxima_entrada = widget_atual.master.nametowidget(widget_atual.tk_focusNext())
    if proxima_entrada:
        proxima_entrada.focus_set()
    
    if widget_atual == entrada3:
        comparador()
    

def comparador():
    senha = entrada2.get()
    senha_repetida = entrada3.get()
    if senha == senha_repetida:
        print("Cadastrado")
    else:
        print("Senhas não coincidem")

root = tk.Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()

ttk.Label(frm, text="Cadastro", font=("ComicSans", 16, "bold")).grid(column=0, row=0)
ttk.Label(frm, text='').grid(column=0, row=1)
ttk.Label(frm, text="Usuário:", font=("ComicSans", 11)).grid(column=0, row=3, sticky='w')

entrada = ttk.Entry(frm, width=30)
entrada.grid(column=0, row=4)
entrada.bind('<Return>', prox)

ttk.Label(frm, text='').grid(column=0, row=5)

ttk.Label(frm, text="Senha:", font=("ComicSans", 11)).grid(column=0, row=6, sticky='w')

entrada2 = ttk.Entry(frm, width=30)
entrada2.grid(column=0, row=7)
entrada2.bind('<Return>', prox)

ttk.Label(frm, text='').grid(column=0, row=8)

ttk.Label(frm, text="Reescreva sua senha:", font=("ComicSans", 11)).grid(column=0, row=9, sticky='w')

entrada3 = ttk.Entry(frm, width=30)
entrada3.grid(column=0, row=10)
entrada3.bind('<Return>', prox)

root.mainloop()
