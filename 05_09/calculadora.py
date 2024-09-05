import customtkinter as ctk
from PIL import Image, ImageTk

# Inicializa a aplicação
app = ctk.CTk()
app.geometry('400x600')
app.configure(fg_color='#1E1E1E')
app.title('Calculadora')

app.columnconfigure(0, weight=0)
app.columnconfigure(1, weight=0)
app.columnconfigure(2, weight=0)
app.columnconfigure(3, weight=0)

app.rowconfigure(0, weight=0)
app.rowconfigure(1, weight=0)
app.rowconfigure(2, weight=0)
app.rowconfigure(3, weight=0)
app.rowconfigure(4, weight=0)
app.rowconfigure(5, weight=0)

but_cor = '#333333'
but_hov = '#4D4D4D' 
text_cor = '#FFFFFF'

resp_frm = ctk.CTkFrame(app, height=150, fg_color='#333333')
resp_frm.grid(row=0, column=0, columnspan=4, sticky='new', pady=0, padx=3)

porc_but = ctk.CTkButton(app, text='%', height=50, width=95 , font=('Segoe UI', 24))
porc_but.grid(row=1, column=0, padx=(3,2), pady=10, sticky='w')

ce_but = ctk.CTkButton(app, text='CE', height=50, width=95 , font=('Segoe UI', 24))
ce_but.grid(row=1, column=1, padx=2, pady=10)

c_but = ctk.CTkButton(app, text='C', height=50, width=95 , font=('Segoe UI', 24))
c_but.grid(row=1, column=2, padx=2, pady=10)

apagar_but = ctk.CTkButton(app, text='<', height=50, width=95 , font=('Segoe UI', 24))
apagar_but.grid(row=1, column=3, padx=(3,2), pady=10, sticky='e')







app.mainloop()