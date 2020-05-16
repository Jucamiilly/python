
import re

print("[+]    Checkpoint 2 created by Julia")


leak={"exe":["exe@exe.com"]}

def cadastroEmail(emails):

    index = 0
    while index < 1:
        tag = input("Qual a tag do dicionario? ").lower()
        email = input("Insira o e-mail: ").lower()
        if re.match(r"[^@]+@[^@]+.[^@]+", email):
            emails[tag] = [email]
            index += 1
        else:
            print("Insira um e-mail valido.")


def buscaEmail(emails):
    print("\n\n-----------------------------------------------------------------------------------------\n")
    print("Descubra se seu e-mail foi vazado!\n")

    busca = input("Insira a tag do dicionario: ").lower()
    lista = emails.get(busca)
    if lista != None:
        print("Seu email foi vazado!")
        print("\nEmail.......", lista[0])
    else:
        print("Seu email nao foi vazado!")

cadastroEmail(leak)

buscaEmail(leak)