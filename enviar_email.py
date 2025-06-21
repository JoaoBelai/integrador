import smtplib
import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8", newline="") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        linha_atual = 0

        for linha in leitor:
            linha_atual +=1
            if linha_atual == 2:
                return linha

    return None

servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
servidor_email.starttls()
servidor_email.login('joaopbelai@gmail.com', 'rrsp cszq jkom naej')

remetente = 'joaopbelai@gmail.com'
destinatarios = ['pedro.carreteiro@aluno.senai.br']
conteudo = ler_csv("LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv")

data = conteudo[0]
hora = conteudo[1]
valor_esteira1 = conteudo[2]
valor_esteira2 = conteudo[3]
valor_esteira3 = conteudo[4]

mensagem = (f"Estoque atualizado com sucesso!"
            f"\nData: {data}"
            f"\nHora da checagem: {hora}"
            f"\nEsteira 1: {valor_esteira1}"
            f"\nEsteira 2: {valor_esteira2}"
            f"\nEsteira 3: {valor_esteira3}")


servidor_email.sendmail(remetente, destinatarios, mensagem)
servidor_email.quit()
