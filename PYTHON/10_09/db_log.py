import customtkinter as ctk
import mysql.connector as mysql

app = ctk.CTk()
app.geometry('600x600')
app.configure(fg_color='#1E1E1E')
app.title('Cadastro')

app.columnconfigure(0, weight=1)
app.columnconfigure(2, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(2, weight=1)

frame_cad = ctk.CTkFrame(app, height=500, width=400, fg_color='gray')
frame_cad.grid(column=1, row=1, sticky='nsew')

frame_cad.pack_propagate(False)
frame_cad.columnconfigure(0, weight=1)
frame_cad.columnconfigure(2, weight=1)

ttl = ctk.CTkLabel(frame_cad, text='LOGIN', font=('Segoe UI', 40, 'bold'), text_color='white')
ttl.pack(anchor='center')

def entry_padrao (nome, texto):
    nl=(f'{nome}_lbl')

    nl = ctk.CTkLabel(frame_cad, text=texto, font=('Segoe UI', 20), text_color='#1E1E1E')
    nl.pack(anchor='w', padx=10, pady=(20, 0))

entry_padrao('user', 'Usuário')
usere = ctk.CTkEntry(frame_cad, width=380)
usere.pack(anchor = 'w', padx=10)

entry_padrao('sen1', 'Senha:')
sen1e = ctk.CTkEntry(frame_cad, width=380)
sen1e.pack(anchor = 'w', padx=10)

# entry_padrao('sen2', 'Reescreva sua senha:')
# sen2e = ctk.CTkEntry(frame_cad, width=380)
# sen2e.pack(anchor = 'w', padx=10)

configDB = {
    'host':'10.28.2.62',
    'user':'suporte',
    'password':'suporte',
    'database':'logdesk'
    }

# db = mysql.connect(**configDB)
# cursor = db.cursor()

# def get():
#     user = usere.get()
#     passw = sen1e.get()
#     logintodb(user, passw)

# def logintodb (user, passw):
#     usuario = 'select nome from cadastro'
    
#     cursor.execute(usuario)
#     resultado = cursor.fetchall()
#     for x in resultado:
#         if x == user:
#             print('hehehe', resultado)
#         else: print('awooooo')

      

# def logintodb(user, passw):
     
#     if passw:
#         db = mysql.connect(**configDB)
#         cursor = db.cursor()
         
    
    
#     else:
#         db = mysql.connect(**configDB)
#         cursor = db.cursor()
         
    
#     savequery = "select * from cadastro"
     
#     try:
#         cursor.execute(savequery)
#         myresult = cursor.fetchall()
       
#         for x in myresult:
#             print(x)
#             print("Query Excecuted successfully")
         
#     except:
#         db.rollback()
#         print("Error occured")



but_log = ctk.CTkButton(frame_cad, text='Logar', fg_color='green', font=('Segoe UI', 20, 'bold'), text_color='white', height=40, width=130)
but_log.pack(pady=(80, 0), padx=10, anchor = 's')



app.mainloop()
