import tkinter as tk

def cores(cor):
    janela.config(bg=cor)
    msg.config(bg=cor, fg='white')

def segredo():
    global looping
    if not looping:
        looping = True
        mudar_cor(0)  # Começa o loop de cores
    else:
        looping = False

def mudar_cor(index):
    if looping:
        cores_lista = [
            'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 
            'magenta', 'pink', 'lightblue', 'lime', 'indigo', 'violet', 
            'turquoise', 'salmon', 'gold', 'silver', 'coral', 'crimson'
        ]
        cor = cores_lista[index % len(cores_lista)]
        cores(cor)
        janela.after(10, mudar_cor, index + 1)

looping = False

janela = tk.Tk()
janela.geometry('600x400')

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(4, weight=1)

msg = tk.Label(text='Cores Psicotécnicas', font=('Arial', 26, 'bold'))
msg.grid(row=0, column=1, columnspan=3, sticky="ew", pady=(0, 50))

b1 = tk.Button(text='   R   ', font=('Arial', 16, 'bold'), command=lambda: cores('red'), fg='red')
b1.grid(row=1, column=1, padx=5, pady=75)

b2 = tk.Button(text='   G   ', font=('Arial', 16, 'bold'), command=lambda: cores('green'), fg='green')
b2.grid(row=1, column=2, padx=5, pady=75)

b3 = tk.Button(text='   B   ', font=('Arial', 16, 'bold'), command=lambda: cores('blue'), fg='blue')
b3.grid(row=1, column=3, padx=5, pady=75)

party = tk.Button(text='   ?   ', font=('Arial', 16, 'bold'), bg='gray', fg='white', command=segredo)
party.grid(row=2, column=2, padx=5, pady=10)

janela.mainloop()
