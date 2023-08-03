# If e Else
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else: 
    print("Saldo insuficiente")

opção = int(input("Informe uma opção [1] Sacar \n[2] Extrato: "))

#   Elif
if opção == 1:
    valor = float(input("Informe a quantia para o saque"))
elif opção == 2:
    print("Exibindo o extrato...")
else: 
    print("Opção inválida")

# If Aninhado 
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!")

# If Ternário
saldo = 200
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque")