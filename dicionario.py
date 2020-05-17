import re

print("[+] Checkpoint 2 created by =Julia=")
leak={"exe":["exe@exe.com"]}
leak["gmail"]=["exe@gmail.com"]
leak["outlook"]=["exe@outlook.com"]
leak["yahoo"]=["exe@yahoo.com"]
leak["hotmail"]=["exe@hotmail.com"]


def menu(leak):
    print("Escolha uma das opções abaixo:\n")
    print("Exibir todos os emails presentes no Banco de Dados(1)\n")
    print("Cadastrar novos emails no Banco de dados(2)\n")
    print("Buscar emails no banco de dados(3)\n")
    print("Sair(4)\n")
    escolha = int(input("\nEscolha sua opção: "))

    if escolha == 1:
        exibirEmails(leak)
    elif escolha == 2:
        cadastroEmail(leak)
    elif escolha == 3:
        buscaEmail(leak)
    elif escolha== 4:
        exit(leak)
    

def exibirEmails(leak):
    for tag, dados in leak.items():
            print("\nTag.....", tag)
            print("Email.....", dados[0])

    menu(leak)

def cadastroEmail(emails):
    index = 0
    while index < 1:
        tag = input("Qual a tag do dicionario? ")
        email = input("Insira o e-mail: ").lower()
        if re.match(r"[^@]+@[^@]+.[^@]+", email):
            emails[tag] = [email]
            index += 1
        else:
            print("Insira um e-mail valido.")


    menu(leak)

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


    menu(leak) 

menu(leak)
