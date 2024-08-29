import tkinter as tk
from tkinter import font

# Inicializar o Tkinter
root = tk.Tk()

# Listar fontes disponíveis
fonts = font.families()
for font_name in fonts:
    print(font_name)

root.destroy()
