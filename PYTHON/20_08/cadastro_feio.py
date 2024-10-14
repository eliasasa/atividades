import tkinter as tk


def conf():
    x=sene.get()
    y=sene2.get()
    z=len(usere.get())
    if x != y or len(x) == 0 or len(y) == 0:
        msg=tk.Label(text='Senhas não correspondem!', fg='red', bg='#1b1e23')
        msg.pack()
        msg.after(1000 , lambda: msg.destroy())
        if z == 0:
            msg2=tk.Label(text='Nome de usuário não pode estar vazio!', fg='red', bg='#1b1e23')
            msg2.pack()
            msg2.after(1000 , lambda: msg2.destroy())
    elif z == 0:
        msg=tk.Label(text='Nome de usuário não pode estar vazio!', fg='red', bg='#1b1e23')
        msg.pack()
        msg.after(1000 , lambda: msg.destroy())
    else:
        msg=tk.Label(text='Cadastro realizado!', fg='green', bg='#1b1e23')
        msg.pack(padx=10, pady=10)
        cadas.after(0, lambda: cadas.destroy())
        usere.config(state='disabled', bg='gray')
        sene.config(state='disabled', bg='gray')
        sene2.config(state='disabled', bg='gray')

        

janela=tk.Tk()
janela.geometry('400x400')
janela.config(bg='#1b1e23')

titulo=tk.Label(text='CADASTRO', font=('Arial', 16, 'bold'), fg='white', bg='#1b1e23')
titulo.pack(padx=10, pady=10)

user=tk.Label(text='Usuário:', font=('Arial', 11), fg='white', bg='#1b1e23')
user.pack(padx=10, pady=0, anchor="w")

usere=tk.Entry(width=70, bg='#2c3e50', fg='white')
usere.pack(padx=10, pady=(0, 10), anchor="w")

sen=tk.Label(text='Senha:', font=('Arial', 11), fg='white', bg='#1b1e23')
sen.pack(padx=10, pady=0, anchor="w")

sene=tk.Entry(width=70, bg='#2c3e50', fg='white')
sene.pack(padx=10, pady=(0, 10), anchor="w")

sen2=tk.Label(text='Reescreva sua senha:', font=('Arial', 11), fg='white', bg='#1b1e23')
sen2.pack(padx=10, pady=0, anchor="w")

sene2=tk.Entry(width=70, bg='#2c3e50', fg='white')
sene2.pack(padx=10, pady=(0, 10), anchor="w")

cadas=tk.Button(text='Cadastrar', font=('Aria', 11, 'bold'), command=conf)
cadas.pack(padx=10, pady=30)

janela.mainloop()