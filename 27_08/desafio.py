import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

app = ctk.CTk()
app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}+0+0")

app.configure(fg_color='black')

titulo = ctk.CTkLabel(app, text="Le Gourmet d'Éderson", font=('Century Gothic', 60, 'italic'))
titulo.pack(padx=30, pady=(25, 0), anchor="w")

image_path = "27_08/vinho massa.jpg"
image = Image.open(image_path)
max_width = int(app.winfo_screenwidth() * 0.9)
max_height = int(app.winfo_screenheight() * 0.9)
image.thumbnail((max_width, max_height))

tk_image = ImageTk.PhotoImage(image)
imagemCtk = ctk.CTkLabel(app, image=tk_image, text='')
imagemCtk.pack(anchor="w", padx=0, pady=(10, 10))

frame_cadastro = ctk.CTkFrame(app, width=600, height=600, corner_radius=10, fg_color='white')
frame_cadastro.place(relx=0.95, rely=0.25, anchor='ne')

titulo_frame = ctk.CTkLabel(frame_cadastro, text="Cadastro", font=('Century Gothic', 40, 'bold'), text_color='black')
titulo_frame.pack(padx=100, pady=(30, 10), anchor="n")

user1 = ctk.CTkLabel(frame_cadastro, text="Usuário:", font=('Century Gothic', 20), text_color='black')
user1.pack(padx=20, pady=(20,5), anchor="w")

usere1 = ctk.CTkEntry(frame_cadastro, width=350)
usere1.pack(padx=20, pady=0, anchor = 'w')

senha1 = ctk.CTkLabel(frame_cadastro, text="Senha:", font=('Century Gothic', 20), text_color='black')
senha1.pack(padx=20, pady=(10,5), anchor="w")

senhere1 = ctk.CTkEntry(frame_cadastro, width=350)
senhere1.pack(padx=20, pady=0, anchor = 'w')

senha2 = ctk.CTkLabel(frame_cadastro, text="Reescreva sua senha:", font=('Century Gothic', 20), text_color='black')
senha2.pack(padx=20, pady=(10,5), anchor="w")

senhere2 = ctk.CTkEntry(frame_cadastro, width=350)
senhere2.pack(padx=20, pady=(0,50), anchor = 'w')

app.mainloop()
