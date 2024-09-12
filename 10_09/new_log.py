import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector as mysql

configDB = {
    'host': '10.28.2.62',
    'user': 'elias',
    'password': 'suporte',
    'database': 'logdesk'
} 

db = mysql.connect(**configDB)
cursor = db.cursor()

def show_text(id):
    search_text = f'SELECT texto FROM cadastro WHERE id_cli = {id}'
    cursor.execute(search_text, id)
    resultado2 = cursor.fetchall()
    print(resultado2)
    ctk.CTkLabel(frame_cad, text=resultado2, font=('', 30)).pack()

def log_user(nome, senha):
    search_user = f'SELECT id_cli FROM cadastro WHERE nome = "{nome}" AND senha = "{senha}"'
    cursor.execute(search_user)
    resultado = cursor.fetchone()
    print(resultado)
    if len(resultado) > 0:
        for widget in frame_cad.winfo_children():
            widget.destroy()
        
    else: pass

def get_info():
    nome_user = usere.get().replace(';', '')
    senha_user = sen1e.get().replace(';', '')


    log_user(nome_user, senha_user)

app = ctk.CTk()
app.geometry('600x600')
app.configure(fg_color='#2C2F33')
app.title('Cadastro')

app.columnconfigure(0, weight=1)
app.columnconfigure(2, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(2, weight=1)

frame_cad = ctk.CTkFrame(app, height=500, width=400, fg_color='#23272A')
frame_cad.grid(column=1, row=1, sticky='nsew')

frame_cad.pack_propagate(False)
frame_cad.columnconfigure(0, weight=1)
frame_cad.columnconfigure(2, weight=1)

ttl = ctk.CTkLabel(frame_cad, text='Textinattor', font=('Segoe UI', 40, 'bold'), text_color='#7289DA')
ttl.pack(anchor='center', pady=(20, 10))

ttl_log = ctk.CTkLabel(frame_cad, text='LOGIN', font=('Segoe UI', 20, 'bold'), text_color='gray')
ttl_log.pack(anchor='w', pady=(10, 5), padx=20)

def entry_padrao(nome, texto):
    nl = ctk.CTkLabel(frame_cad, text=texto, font=('Segoe UI', 20), text_color='#DCDDDE')
    nl.pack(anchor='w', padx=20, pady=(10, 0))

entry_padrao('user', 'Usuário')
usere = ctk.CTkEntry(frame_cad, width=380, fg_color='#99AAB5', text_color='#2C2F33', font=('Segoe UI', 14))
usere.pack(anchor='w', padx=20, pady=(0, 30))

entry_padrao('sen1', 'Senha:')
sen1e = ctk.CTkEntry(frame_cad, width=380, fg_color='#99AAB5', text_color='#2C2F33', font=('Segoe UI', 14), show="*")
sen1e.pack(anchor='w', padx=20, pady=(0, 10))

eye_op_path = Image.open('10_09/icon/codicon--eye-closed.png')
eye_op_img = eye_op_path.resize((50, 50))
eye_op_img = ImageTk.PhotoImage(eye_op_img)

eye = ctk.CTkLabel(frame_cad, image=eye_op_img, text='')
eye.pack(anchor='e', pady=0, padx=20)
eye.image = eye_op_img

def alter_sen(event, nome):
    if nome.cget('show') == '*':
        eye_path_new = Image.open('10_09/icon/codicon--eye.png')
        eye_img_new = eye_path_new.resize((50, 50))
        eye_img_new = ImageTk.PhotoImage(eye_img_new)
        nome.configure(show='') 
    else:
        eye_path_new = Image.open('10_09/icon/codicon--eye-closed.png')
        eye_img_new = eye_path_new.resize((50, 50))
        eye_img_new = ImageTk.PhotoImage(eye_img_new)
        nome.configure(show='*')

    event.widget.configure(image=eye_img_new)
    event.widget.image = eye_img_new

eye.bind("<Button-1>", lambda event: alter_sen(event, sen1e))

but_log = ctk.CTkButton(frame_cad, text='Logar', fg_color='#7289DA', hover_color='#677BC4', font=('Segoe UI', 20, 'bold'), text_color='white', height=50, width=160, command=get_info)
but_log.pack(pady=(30, 0), padx=20, anchor='center')

texto_lbl = ctk.CTkLabel(frame_cad, text='Não tem uma conta?', font=('Segoe UI', 15), text_color='white')
texto_lbl.pack(anchor='center', padx=10, pady=(10,0))

cad_lbl = ctk.CTkLabel(frame_cad, text='Cadastrar', font=('Segoe UI', 15, 'bold'), text_color='#7289DA')
cad_lbl.pack(anchor='center', padx=10, pady=0)

def dt_log(event):
    frame_cad.configure(fg_color='#23272A')
    app.configure(fg_color='#2C2F33')
    ttl.configure(text_color='#7289DA')
    ttl_log.configure(text='LOGIN', text_color='gray')
    but_log.configure(text='Logar', fg_color='#7289DA', hover_color='#677BC4')
    texto_lbl.configure(text='Não tem uma conta?', text_color='white')
    cad_lbl.configure(text='Cadastrar', text_color='#7289DA')
    
    usere.configure(fg_color='#99AAB5', text_color='#2C2F33')
    sen1e.configure(fg_color='#99AAB5', text_color='#2C2F33')

    cad_lbl.unbind("<Button-1>")
    cad_lbl.bind("<Button-1>", dt_cad)

def dt_cad(event):
    frame_cad.configure(fg_color='#2F3136')
    app.configure(fg_color='#23272A')
    ttl.configure(text_color='#FF4500')
    ttl_log.configure(text='CADASTRO')
    but_log.configure(text='Cadastrar', fg_color='#FF4500', hover_color='#FF8C00')
    texto_lbl.configure(text='Já tem uma conta?', text_color='#FFFFFF')
    cad_lbl.configure(text='Logar', text_color='#FF4500')

    usere.configure(fg_color='#4B5159', text_color='#E4E6E9')
    sen1e.configure(fg_color='#4B5159', text_color='#E4E6E9')

    cad_lbl.unbind("<Button-1>")
    cad_lbl.bind("<Button-1>", dt_log)

cad_lbl.bind("<Button-1>", dt_cad)

app.mainloop()

db.close()
