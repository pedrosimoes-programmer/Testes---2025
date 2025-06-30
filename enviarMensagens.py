import pyautogui
import time 
import random

pyautogui.PAUSE = 0.5

def abrirZap(): 
    pyautogui.press("win")
    pyautogui.write("whats")
    pyautogui.press("enter")

def enviarMsg(nome):
    pyautogui.write(nome)
    pyautogui.click(209, 210) # -> Clica na pessoa pesquisada
    pyautogui.press("enter")
    pyautogui.write("Teste")
    pyautogui.press("enter")

aleatorioNumero = random.randint(1, 9)
print(aleatorioNumero)

abrirZap()
time.sleep(3)

if aleatorioNumero >= 1 and aleatorioNumero < 4:
    enviarMsg("Joao Vitor")

if aleatorioNumero > 3 and aleatorioNumero < 7:
    enviarMsg("Marcello")

if aleatorioNumero > 7:
    enviarMsg("Joao Henrique")
    
#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado