import tkinter as tk
from PIL import Image, ImageTk

def atualizar_imagem(indice):
    global img_tk, ent1, descricao_label  # Inclui descricao_label na lista de variáveis globais
    image_path = imagens[indice]
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Ajusta o tamanho conforme necessário
    img_tk = ImageTk.PhotoImage(img)
    label_imagem.config(image=img_tk)
    label_imagem.image = img_tk
    
    # Atualiza a descrição correspondente
    descricao_atual = descricoes[indice]
    ent1.delete(0, tk.END)  # Limpa o conteúdo atual do Entry
    ent1.insert(0, descricao_atual)  # Insere a nova descrição
    
    # Atualiza a label de descrição, se ela existir
    if descricao_label:
        descricao_label.destroy()  # Remove a label de descrição anterior, se houver

def prox():
    global x
    x += 1
    if x >= len(imagens):
        x = 0
    atualizar_imagem(x)

def ant():
    global x
    x -= 1
    if x < 0:
        x = len(imagens) - 1
    atualizar_imagem(x)

def mostrar_descricao(event):
    global descricao_label
    descricao_atual = ent1.get()
    # Remove o Entry e exibe a Label com a descrição
    ent1.place_forget()
    descricao_label = tk.Label(janela, text=descricao_atual, bg='#AE445A', fg='#451952', font=('Arial', 16))
    descricao_label.place(anchor='center', rely=0.9, relx=0.5)

# Criação da janela principal
janela = tk.Tk()
janela.geometry('500x600')
janela.config(bg='#451952')

# Índice inicial da imagem
x = 0

# Lista de caminhos das imagens
imagens = [
    '22_08/bisnaga.webp',
    '22_08/cellbit.jpg',
    '22_08/image1.jfif',
    '22_08/Internet-O-Filme.jpg',
    '22_08/caveirao.jpg'
]

# Lista de descrições correspondentes
descricoes = [
    'Descrição da imagem 1',
    'Descrição da imagem 2',
    'Descrição da imagem 3',
    'Descrição da imagem 4',
    'Descrição da imagem 5'
]

# Adiciona o título
titulo = tk.Label(text='Galeria', font=('Arial', 36, 'bold'), bg='#451952', fg='white')
titulo.place(anchor='center', relx=0.5, rely=0.05)

# Botões de navegação
bdire = tk.Button(text='   <   ', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=ant)
bdire.place(anchor='w', relx=0, rely=0.5)

besq = tk.Button(text='   >   ', font=('Arial', 16, 'bold'), bg='#F39F5A', fg='white', command=prox)
besq.place(anchor='e', relx=1, rely=0.5)

# Adiciona o widget Label para a imagem
img_tk = None
label_imagem = tk.Label(janela)
label_imagem.place(anchor='center', relx=0.5, rely=0.5)

# Adiciona o Entry para a descrição
ent1 = tk.Entry(janela, width=35, bg='#AE445A', fg='#451952', font=('Arial', 16))
ent1.place(anchor='center', rely=0.9, relx=0.5)

# Inicializa a label de descrição como None
descricao_label = None

# Atualiza a imagem e a descrição inicial
atualizar_imagem(x)

# Bind do evento <Return> para o Entry
ent1.bind('<Return>', mostrar_descricao)

# Inicia o loop principal da interface gráfica
janela.mainloop()
