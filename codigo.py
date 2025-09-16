import pyautogui
import time


# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas
# pyautogui.PAUSE-> espera um delay entre cada código
# pyautogui - > fazer automações com python

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o navegador

pyautogui.press("win") # escolho a tecla na qual ele deve apertar
pyautogui.write("opera") # ele escreve o que está escrito dentro do parênteses
pyautogui.press("enter")

# digitar o site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login

pyautogui.click(x=838, y=459)
pyautogui.write("emaillegal")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("senhalegal")

# botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar 1 produto
for linha in tabela.index: # para cada linha da minha tabela
    
    pyautogui.click(x=794, y=306)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") # passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar para o proximo campo
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab") # passar para o proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    
    pyautogui.press("tab") # passar para o proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    
    pyautogui.press("tab") # passar para o proximo campo
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab") # passar para o proximo campo
    pyautogui.press("enter")


    # número positivo - scroll para cima
    # número negativo - scroll para baixo
    pyautogui.scroll(10000)




# Passo 5: Repetir para todos os produtos