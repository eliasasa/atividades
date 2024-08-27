import tkinter as tk

# Inicializar o Tkinter
root = tk.Tk()

# Listar fontes disponíveis
fonts = tk.font.families()
for font in fonts:
    print(font)

root.destroy()
