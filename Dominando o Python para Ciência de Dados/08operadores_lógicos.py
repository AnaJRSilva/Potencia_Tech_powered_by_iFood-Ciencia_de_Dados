saldo = 1000
saque = 200
limite = 100

# Operador E: ambos precisam ser verdadeiros
print (saldo >= saque and saque <= limite) 

# Operador OU: apenas um precisa ser verdadeiro
print (saldo >= saque or saque <= limite) 

# Operador de Negação: o contrário do resultado 
contatos_emergencia = []

print (not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500")
print(not "")

# Parênteses
conta_especial = True

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

saldo_aprovado = saldo >= saque and saque <= limite
saldo_especial = conta_especial and saldo >= saque
print (saldo_aprovado or saldo_especial)

resultado = saldo_aprovado or saldo_especial
print (resultado)
