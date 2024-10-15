import customtkinter as ctk
from PIL import Image, ImageTk
import mysql.connector as mysql

class FofoqueiroApp:

    def __init__(self):
        # Configuração da janela principal
        self.app = ctk.CTk()
        self.app.geometry(f"{self.app.winfo_screenwidth()}x{self.app.winfo_screenheight()}")
        self.app.configure(fg_color='#1F1B24')
        self.app.title('Fofoqueiro')
        self.app.state('zoomed')
        self.app.columnconfigure(0, weight=1)
        self.app.columnconfigure(2, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.app.rowconfigure(2, weight=1)
        
        self.label_ex= ['fofoca1','fofoca2', 'fofoca2']

        self.setup_login_screen()

        self.app.mainloop()

    def setup_login_screen(self):
        # Configuração do frame de login
        self.frame_cad = ctk.CTkFrame(self.app, height=500, width=400, fg_color='#2A2731')  # Fundo escuro e misterioso
        self.frame_cad.grid(column=1, row=1, sticky='nsew')
        self.frame_cad.pack_propagate(False)
        self.frame_cad.grid_propagate(False)
        self.frame_cad.columnconfigure(0, weight=1)
        self.frame_cad.columnconfigure(2, weight=1)

        # Título principal
        ttl = ctk.CTkLabel(self.frame_cad, text='Ofuxico', font=('Segoe UI', 42, 'bold'), text_color='#FF6F91')  # Cor vibrante
        ttl.pack(anchor='center', pady=(20, 10))

        # Subtítulo de login
        ttl_log = ctk.CTkLabel(self.frame_cad, text='LOGIN', font=('Segoe UI', 20, 'bold'), text_color='#F7D488')  # Dourado suave
        ttl_log.pack(anchor='w', pady=(10, 5), padx=20)

        # Entrada de usuário
        self.entry_padrao('user', 'Usuário')
        self.usere = ctk.CTkEntry(self.frame_cad, width=380, fg_color='#FFC1E3', text_color='#2C2F33', font=('Segoe UI', 14))  # Rosa pastel suave
        self.usere.pack(anchor='w', padx=20, pady=(0, 30))

        # Entrada de senha
        self.entry_padrao('sen1', 'Senha:')
        self.sen1e = ctk.CTkEntry(self.frame_cad, width=380, fg_color='#FFC1E3', text_color='#2C2F33', font=('Segoe UI', 14), show="*")
        self.sen1e.pack(anchor='w', padx=20, pady=(0, 10))

        # Ícone de olho para exibir/ocultar senha
        eye_op_path = Image.open('16_09/icons/codicon--eye-closed.png')
        eye_op_img = eye_op_path.resize((50, 50))
        self.eye_op_img = ImageTk.PhotoImage(eye_op_img)

        self.eye = ctk.CTkLabel(self.frame_cad, image=self.eye_op_img, text='')
        self.eye.pack(anchor='e', pady=0, padx=20)
        self.eye.image = self.eye_op_img
        self.eye.bind("<Button-1>", lambda event: self.alter_sen(event, self.sen1e))

        self.option_menu = ctk.CTkOptionMenu(self.frame_cad, values=["Não logado", "Cliente", "Famoso", "ADM"], fg_color='#FFB6C1', button_color='#FF6347', button_hover_color='#FF7F50', dropdown_fg_color='#FFE4E1', dropdown_hover_color='#FF4500', dropdown_text_color='#2F4F4F', text_color='#FFFFFF', font=("Segoe UI", 16, 'bold'))
        self.option_menu.pack(pady=(20, 0), anchor='e', padx=20)

        # Botão de login
        but_log = ctk.CTkButton(self.frame_cad, text='Logar', fg_color='#FF6F91', hover_color='#F06292', font=('Segoe UI', 20, 'bold'), text_color='white', height=50, width=160, command=self.login)
        but_log.pack(pady=(30, 0), padx=20, anchor='center')
    
    def home(self):
        self.frame = ctk.CTkFrame(self.app, width=1152, height=864, fg_color='#2A2731')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)

        self.frame.columnconfigure(2, weight=1)
        self.create_content()

    def create_content(self):
        index = 0
        for index, i in enumerate(self.label_ex):
            ctk.CTkLabel(self.frame, text=f"Item {i}", font=('Segoe UI', 20, 'bold'), text_color='#FFFFFF').grid(row=index, column=0, pady=15, padx=20, sticky='w')
            button = ctk.CTkButton(self.frame, text=f'Ver {i}', text_color='#EAEAEA', fg_color='#3B3A43', hover_color='#4B4A55', font=('Segoe UI', 20, 'bold'), width=200, height=55, corner_radius=10)
            button.grid(row=index, column=2, pady=(10, 0), padx=10, sticky='e')
            if index % 2 != 0:
                button.configure(fg_color='#4A4A5A', hover_color='#5A5A6A')
            else: pass
    
    def limpar_tela(self):
        for widget in self.app.winfo_children():
            widget.destroy()

    def login(self):
        tipo = self.option_menu.get()
        if tipo == 'Não logado':
            self.limpar_tela()
            self.home()


    def entry_padrao(self, nome, texto):
        nl = ctk.CTkLabel(self.frame_cad, text=texto, font=('Segoe UI', 20), text_color='#F7D488')  # Dourado suave
        nl.pack(anchor='w', padx=20, pady=(10, 0))

    def alter_sen(self, event, nome):
        if nome.cget('show') == '*':
            eye_path_new = Image.open('16_09/icons/codicon--eye.png')
            eye_img_new = eye_path_new.resize((50, 50))
            eye_img_new = ImageTk.PhotoImage(eye_img_new)
            nome.configure(show='') 
        else:
            eye_path_new = Image.open('16_09/icons/codicon--eye-closed.png')
            eye_img_new = eye_path_new.resize((50, 50))
            eye_img_new = ImageTk.PhotoImage(eye_img_new)
            nome.configure(show='*')

        event.widget.configure(image=eye_img_new)
        event.widget.image = eye_img_new

# Executar a aplicação
if __name__ == "__main__":
    app = FofoqueiroApp()
