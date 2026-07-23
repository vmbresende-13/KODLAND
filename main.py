import time
import random

print("Bem vindo a biblioteca da definição das girias jovens")

time.sleep(1)

gj = {
    "Stalkear": "investigar a vida de alguém online",
    "CRINGE": "algo vergonhoso ou constrangedor",
    "VDD": "abreviação da palavra verdade",
    "BISCOITAR": "postar algo apenas para chamar a atenção",
    "HATER": "pessoa que está constantemente criticando os outros",
    "VLW": "abreviação da palavra valeu",
}

for giria in random.sample(list(gj.keys()), 5):
    print(giria, "-", gj[giria])

time.sleep(1)

ad = input("Deseja adicionar alguma outra giria? s / n ")

if ad == "s":
    nome = input("Digite a giria: ")
    significado = input("Digite o significado: ")

    gj[nome] = significado

    print("Giria adicionada com sucesso!")
    print(nome, "-", gj[nome])

else:
    print("Programa encerrado.")

print("Girias sorteadas novamente:")

for giria in random.sample(list(gj.keys()), 5):
    print(giria, "-", gj[giria])
