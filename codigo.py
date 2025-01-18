#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#passo 1 - abrir o OperaGX e entrar no link do banco de dados
#passo 2 - dar login no banco de dados
#passo 3 - cadastrar os produtos

import pyautogui
import pandas
import time

#abre navegador
pyautogui.press("win")
pyautogui.write("Opera GX")
pyautogui.press("enter")

#entra no site
time.sleep(1.5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Preenche os dados de login
time.sleep(1.5)
pyautogui.click(x=808, y=480)
pyautogui.write("usuario@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaadmin")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(0.5)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=877, y=337)
    
    #Preenche código produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #Preenche marca produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #Preenche tipo produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #Preenche categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #Preenche preco_unitario produto
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #Preenche custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #Preenche obs produto
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #envia produto e volta pro começo
    pyautogui.press("enter")
    pyautogui.scroll(100000000)
