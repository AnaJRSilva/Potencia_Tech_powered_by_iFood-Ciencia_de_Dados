# For Iterável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS: #letra.upper traduz tudo para maiúsculo
        print(letra, end="")
else: # não muito utilizado nesses casos   
    print()

# Função Range (start, stop, step)
for numero in range(0, 51, 5):
    print(numero, end=" ")

# While
opção = -1

while opção != 0:
    opção = int(input("[1] Saca \n[2] Extrato \n[0] Sair \n: "))

    if opção == 1:
        print("Sacando...")
    elif opção == 2:
        print("Exibindo o extrato")

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break #ou continue, caso você queira pular uma execução 

    print(numero)


