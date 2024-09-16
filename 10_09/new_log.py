import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector as mysql

configDB = {
    'host': '10.28.2.62',
    'user': 'suporte',
    'password': 'suporte',
    'database': 'logdesk'
} 

db = mysql.connect(**configDB)
cursor = db.cursor()

global Cadastro
Cadastro = False

def entry_padrao(nome, texto):
    nl = ctk.CTkLabel(frame_cad, text=texto, font=('Segoe UI', 20), text_color='#DCDDDE')
    nl.pack(anchor='w', padx=20, pady=(10, 0))

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

def show_text(id):
    frame_cad.update_idletasks()
    search_text = 'SELECT texto FROM cadastro WHERE id_cli = %s'
    cursor.execute(search_text, (id,))
    resultado2 = cursor.fetchone() 

    if resultado2:
        texto, = resultado2
        ctk.CTkLabel(frame_cad, text='Seu texto:', font=('Segoe UI', 40, 'bold'), text_color='#7289DA').pack(anchor='center', pady=(20, 10))
        ctk.CTkLabel(frame_cad, text=texto, font=('Segoe UI', 30)).pack(anchor='n', pady=20)

        ctk.CTkButton(frame_cad, text='Voltar', height=40, width=140, fg_color='#FF6F61', hover_color='#FF8E8B', font=('Segoe UI', 14, 'bold'), text_color='white', corner_radius=8, border_width=2, border_color='#FF5C5C', command=initialize_login_screen).place(relx=0.5, rely=0.85, anchor='center')
    else:
        show_error_message('Texto não encontrado para esse ID.')


def log_user(nome, senha):
    search_user = 'SELECT id_cli FROM cadastro WHERE nome = %s AND senha = %s'
    cursor.execute(search_user, (nome, senha))
    resultado = cursor.fetchone()

    if resultado:
        for widget in frame_cad.winfo_children():
            widget.destroy()
        show_text(resultado[0]) 
    else:
        show_error_message('Usuário não encontrado!')


def return_log():
    global Cadastro
    Cadastro = False
    for widget in app.winfo_children():
        widget.destroy()

    fpag = ctk.CTkFrame(app, width=200, height=200, corner_radius=10, fg_color='green')
    fpag.grid(column=1, row=1)
    checkimg = Image.open('10_09/icon/gg--check-o.png')
    checkimg = ImageTk.PhotoImage(checkimg)
    fplab = ctk.CTkLabel(fpag, image=checkimg, text='')
    fplab.pack(padx=20, pady=20)
    msgf = ctk.CTkLabel(fpag, text='Cadastro realizado!\nVoltando para o login.', font=('Arial', 18, 'bold'), text_color='white')
    msgf.pack(padx=20, pady=20)        
    fpag.after(3000, fpag.destroy)
    frame_cad.after(3000, initialize_login_screen)

    

def cad_user():
    texto = textbox.get("1.0", "end").strip().replace(';', '.')

    insert_user = 'INSERT INTO cadastro VALUES (null, %s, %s, %s)'
    
    if not texto:
        show_error_message('Campo de texto não pode estar vazio!')
    else:
        cursor.execute(insert_user, (nome_user, senha_user, texto))
        db.commit()
        print("Usuário cadastrado com sucesso!")
        texto = ''
        return_log()

def text_box():
    global textbox
    Cadastro = False
    text_lbl = ctk.CTkLabel(frame_cad, text='Digite seu texto:', font=('Segoe UI', 30, 'bold'), text_color='#FF4500')
    text_lbl.pack(anchor='center', pady=(20, 10))
    textbox = ctk.CTkTextbox(frame_cad, width=360, height=140, fg_color='#2C2F33', text_color='white', font=('Segoe UI', 14), border_width=2, scrollbar_button_color='#FF4500', scrollbar_button_hover_color='#FF8C00')
    textbox.pack(padx=10, pady=10)
    but_send = ctk.CTkButton(frame_cad, text='Enviar', fg_color='#FF4500', hover_color='#FF8C00', font=('Segoe UI', 16, 'bold'), text_color='white', height=40, width=120, command=cad_user)
    but_send.pack(pady=(10, 0), padx=20, anchor='center')
    ctk.CTkButton(frame_cad, text='Voltar', height=40, width=140, fg_color='#FF6F61', hover_color='#FF8E8B', font=('Segoe UI', 14, 'bold'), text_color='white', corner_radius=8, border_width=2, border_color='#FF5C5C', command=initialize_login_screen).place(relx=0.5, rely=0.85, anchor='center')

def show_error_message(message_text):
    msg_frame = ctk.CTkFrame(frame_cad, fg_color='#3C0D0D', border_width=2, border_color='#E74C3C', corner_radius=10)
    msg_frame.place(relx=0.5, rely=0.65, anchor='center')

    mensagem = ctk.CTkLabel(msg_frame, text=message_text, text_color='#E74C3C', font=('Segoe UI', 16, 'bold'))
    mensagem.pack(padx=20, pady=15)

    msg_frame.after(1000, msg_frame.destroy)

def get_info():
    global nome_user, senha_user
    nome_user = usere.get().replace(';', '')
    senha_user = sen1e.get().replace(';', '')
    if len(nome_user) < 5 and len(senha_user) < 5:
        show_error_message('Senha ou usuário com menos de 5 caracteres!')
    elif len(nome_user) < 5:
        show_error_message(f'Nome de usuário muito curto: {len(nome_user)}/5')
    elif len(senha_user) < 5:
        show_error_message(f'Senha muito curta: {len(senha_user)}/5')
    else:
        if Cadastro == False:
            log_user(nome_user, senha_user)
        else: 
            for widget in frame_cad.winfo_children():
                widget.destroy()
            text_box()

def dt_log(event):
    global Cadastro
    Cadastro = False
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
    global Cadastro
    Cadastro = True
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

def initialize_login_screen():
    global frame_cad, ttl, ttl_log, usere, sen1e, eye, but_log, texto_lbl, cad_lbl
    app.configure(fg_color='#2C2F33')
    frame_cad = ctk.CTkFrame(app, height=500, width=400, fg_color='#23272A')
    frame_cad.grid(column=1, row=1, sticky='nsew')
    frame_cad.pack_propagate(False)
    frame_cad.grid_propagate(False)
    frame_cad.columnconfigure(0, weight=1)
    frame_cad.columnconfigure(2, weight=1)

    ttl = ctk.CTkLabel(frame_cad, text='Textinattor', font=('Segoe UI', 40, 'bold'), text_color='#7289DA')
    ttl.pack(anchor='center', pady=(20, 10))

    ttl_log = ctk.CTkLabel(frame_cad, text='LOGIN', font=('Segoe UI', 20, 'bold'), text_color='gray')
    ttl_log.pack(anchor='w', pady=(10, 5), padx=20)

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

    eye.bind("<Button-1>", lambda event: alter_sen(event, sen1e))

    but_log = ctk.CTkButton(frame_cad, text='Logar', fg_color='#7289DA', hover_color='#677BC4', font=('Segoe UI', 20, 'bold'), text_color='white', height=50, width=160, command=get_info)
    but_log.pack(pady=(30, 0), padx=20, anchor='center')

    texto_lbl = ctk.CTkLabel(frame_cad, text='Não tem uma conta?', font=('Segoe UI', 15), text_color='white')
    texto_lbl.pack(anchor='center', padx=10, pady=(10,0))

    cad_lbl = ctk.CTkLabel(frame_cad, text='Cadastrar', font=('Segoe UI', 15, 'bold'), text_color='#7289DA')
    cad_lbl.pack(anchor='center', padx=10, pady=0)

    cad_lbl.bind("<Button-1>", dt_cad)


app = ctk.CTk()
app.geometry('600x600')
app.configure(fg_color='#2C2F33')
app.title('Cadastro')

app.columnconfigure(0, weight=1)
app.columnconfigure(2, weight=1)
app.rowconfigure(0, weight=1)
app.rowconfigure(2, weight=1)

initialize_login_screen()

app.mainloop()

db.close()
