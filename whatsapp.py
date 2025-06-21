import csv
import pyautogui
import time
import pyperclip

def ler_csv(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8", newline="") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        linha_atual = 0

        for linha in leitor:
            linha_atual +=1
            if linha_atual == 2:
                return linha

    return None

linha = ler_csv("LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv")

data = linha[0]
valor_esteira1 = linha[2]
valor_esteira2 = linha[3]
valor_esteira3 = linha[4]
data = data.replace("/", "-")

verde = "🟢"
amarelo = "🟡"
vermelho = "🔴"

if valor_esteira1 == "3":
    valor_esteira1 = verde
elif valor_esteira1 == "2":
    valor_esteira1 = amarelo
else:
    valor_esteira1 = vermelho

if valor_esteira2 == "3":
    valor_esteira2 = verde
elif valor_esteira2 == "2":
    valor_esteira2 = amarelo
else:
    valor_esteira2 = vermelho

if valor_esteira3 == "3":
    valor_esteira3 = verde
elif valor_esteira3 == "2":
    valor_esteira3 = amarelo
else:
    valor_esteira3 = vermelho

mensagem = f"Estoque em {data}: Esteira 1: {valor_esteira1} | Esteira 2: {valor_esteira2} | Esteira 3: {valor_esteira3}"
pyperclip.copy(mensagem)

time.sleep(7)

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://web.whatsapp.com/")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=391, y=170)
pyautogui.write("anotacoes")
pyautogui.press("enter")
pyautogui.click(x=589, y=173)
pyautogui.click(x=940, y=1006)
time.sleep(4)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")