def depositar(valor):
    saldo = 500
    saldo += valor
    print("Saldo final", saldo)

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa.")
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

depositar(1000) 
sacar(600)