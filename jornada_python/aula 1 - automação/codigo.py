import pyautogui as pg
import time as t
import pandas as p
# pip install pyautogui
# pip install pandas

# Passo 1: Entrar no sistema
# pyautogui.write # -> Escrever
# pyautogui.click # -> Clicar
# pyautogui.press # -> Apertar tecla
# pg.hotkey('alt', 'f4') # -> Atalhos
# pg.click(x=758, y=352, clicks = 3, button='secondary') # Clicar 3 vezes e botão direito >> ('left', 'middle', 'right', 'primary', 'secondary', 1, 2, 3)

# -- Abrir navegadorfelipenetoreal@gmail.com    senha123

# pg.PAUSE = 1 # -> Tempo de 1s em todos os comandos

pg.FAILSAFE = True

pg.click(x=417, y=1064)

# pg.press('win') # -> Botão windows
# pg.write('edge')
# pg.press('enter')

# -- Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

t.sleep(.5)
pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pg.press('enter')

# Passo 2: Fazer login

t.sleep(1.8)
pg.click(x=758, y=352)
pg.write('felipenetoreal@gmail.com')
pg.press('tab') # -> Passa pro próximo campo
pg.write('senha123')
pg.press('enter')
t.sleep(1)
pg.press('tab')

# Passo 3: Importar db

prod = p.read_csv('jornada_python/aula 1 - automação/produtos.csv')


# Passo 4: Cadastrar 1 produto
# Codigo, Marca, Tipo, Categoria, Preço UNI, Custo, OBS

for linha in prod.index:
    codigo = str(prod.loc[linha, 'codigo'])
    pg.write(codigo)
    pg.press('tab')

    marca = prod.loc[linha, 'marca']
    pg.write(marca)
    pg.press('tab')

    tipo = prod.loc[linha, 'tipo']
    pg.write(tipo)
    pg.press('tab')

    categoria = str(prod.loc[linha, 'categoria'])
    pg.write(categoria)
    pg.press('tab')

    preco_unitario = str(prod.loc[linha, 'preco_unitario'])
    pg.write(preco_unitario)
    pg.press('tab')

    custo = str(prod.loc[linha, 'custo'])
    pg.write(custo)
    pg.press('tab')

    obs = prod.loc[linha, 'obs']
    if not p.isna(obs):
        pg.write(str(obs))
    pg.press('tab')
    
    pg.press('enter')
    pg.scroll(5000)
    pg.click(x=792, y=243)

# Passo 5: Repetir o processo

# pg.scroll(5000) # -> Scroll pra cima (baixo = -)