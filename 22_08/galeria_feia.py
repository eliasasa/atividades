import tkinter as tk
from PIL import Image, ImageTk

class Galeria:
    def __init__(self, root):
        self.janela = root
        self.janela.geometry('500x600')
        self.janela.config(bg='#451952')

        self.x = 0
        self.imagens = [
            '22_08/bisnaga.webp',
            '22_08/cellbit.jpg',
            '22_08/image1.jfif',
            '22_08/Internet-O-Filme.jpg',
            '22_08/caveirao.jpg'
        ]

        self.titulos = [
            '',
            '',
            '',
            '',
            ''
        ]

        self.img_tk = None

        self.titulo = tk.Label(self.janela, text='Galeria', font=('Arial', 36, 'bold'), bg='#451952', fg='white')
        self.titulo.place(anchor='center', relx=0.5, rely=0.05)

        self.bdire = tk.Button(self.janela, text='   <   ', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=self.ant)
        self.bdire.place(anchor='w', relx=0, rely=0.5)

        self.besq = tk.Button(self.janela, text='   >   ', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=self.prox)
        self.besq.place(anchor='e', relx=1, rely=0.5)

        self.label_imagem = tk.Label(self.janela)
        self.label_imagem.place(anchor='center', relx=0.5, rely=0.5)

        self.entry_text = tk.Entry(self.janela, width=35, bg='#AE445A', fg='#451952', font=('Arial', 16))
        self.entry_text.place(anchor='center', rely=0.85, relx=0.5)

        self.enviar_btn = tk.Button(self.janela, text='Enviar', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=self.atualizar_titulo)
        self.enviar_btn.place(anchor='center', rely=0.95, relx=0.5)

        self.titulo_imagem = tk.Label(self.janela, text='', font=('Arial', 16, 'bold'), bg='#451952', fg='white')
        self.titulo_imagem.place(anchor='center', rely=0.8, relx=0.5)

        self.atualizar_imagem(self.x)

    def atualizar_imagem(self, indice):
        self.img_tk = None
        image_path = self.imagens[indice]
        img = Image.open(image_path)
        img = img.resize((300, 300))
        self.img_tk = ImageTk.PhotoImage(img)
        self.label_imagem.config(image=self.img_tk)
        self.label_imagem.image = self.img_tk
        self.entry_text.delete(0, tk.END)
        self.titulo_imagem.config(text=self.titulos[indice])

    def prox(self):
        self.x += 1
        if self.x >= len(self.imagens):
            self.x = 0
        self.atualizar_imagem(self.x)

    def ant(self):
        self.x -= 1
        if self.x < 0:
            self.x = len(self.imagens) - 1
        self.atualizar_imagem(self.x)

    def atualizar_titulo(self):
        novo_titulo = self.entry_text.get() 
        self.titulos[self.x] = novo_titulo 
        self.entry_text.delete(0, tk.END) 
        self.titulo_imagem.config(text=novo_titulo)  

if __name__ == '__main__':
    root = tk.Tk()
    app = Galeria(root)
    root.mainloop()
