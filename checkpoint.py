import re

emails = []
index = 0
while index < 30:
    email = input("Insira o e-mail: ").lower()
    if re.match(r"[^@]+@[^@]+.[^@]+", email):
        emails.append(email)
        index += 1
    else:
        print("Insira um e-mail valido.")

busca = input("Insira seu e-mail: ").lower()
if re.match(r"[^@]+@[^@]+.[^@]+", busca):
    for mail in emails:
        if mail == busca:
            print("O email " + busca + " Teve sua senha Vazada")