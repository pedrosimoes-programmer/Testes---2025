#Importa as bibliotecas
import pandas as pd
import pyautogui
import time 
import random

#funções
def abrirZap(): 
    pyautogui.press("win")
    pyautogui.write("whats")
    pyautogui.press("enter")

def enviarMsg():
    pyautogui.write(nome)
    time.sleep(2)
    pyautogui.click(209, 210) # -> Clica na pessoa pesquisada
    linha = random.randint(1, 133)
    país = tabela2.loc[linha, "País"]
    populacao = tabela2.loc[linha, "População"]
    if tabela2.loc[linha, "População"] > 100000000:
        mensagem = f'Ola, {nome}! Voce sabia que o pais {país} tem gente pra caramba! Sim! Sao: {populacao:,} de pessoas!'
    elif tabela2.loc[linha, "População"] < 10000000:
        mensagem = f'Ola, {nome}! Voce sabia que o pais {país} tem gente pra caramba! Sim! Sao: {populacao:,} de pessoas!'
    else:
        mensagem = f'Ola, {nome}! Voce sabia que o pais {país} tem gente pra caramba! Sim! Sao: {populacao:,} de pessoas!'
    pyautogui.write(mensagem)
    pyautogui.press("enter")


tabela2 = pd.read_excel("TabelaTeste2.xlsx")

pyautogui.PAUSE = 0.5

aleatorioNumero = random.randint(1, 900)
print(aleatorioNumero)

if aleatorioNumero >= 1 and aleatorioNumero < 300:
    nome = str("Joao Vitor")

if aleatorioNumero > 300 and aleatorioNumero < 700:
    nome = str("Joao Henrique")

if aleatorioNumero > 700:
    nome = str("Marcello")

abrirZap()
time.sleep(3)
enviarMsg()

#for linha in tabela2.index:

#tabela = pd.read_excel("TabelaTeste.xlsx")

#for linha in tabela.index:
#    if tabela.loc[linha, "Quantidade"] > 5:
#        print("Bastante")
#    else:
#        print("Pouco")