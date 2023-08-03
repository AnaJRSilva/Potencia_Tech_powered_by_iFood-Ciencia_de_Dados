# Identificação
curso = "Curso de Python"
nome_curso = curso 
saldo, limite = 200, 200

print(curso is nome_curso) # mesmo "valor"
print(curso is not nome_curso) # não estão no mesmo ambiente 
print(saldo is limite) 
print(saldo is not limite) 

#Associação 
frutas = ["limão", "maça", "laranja"]
print("laranja" in frutas) #sensivel a letras maiúsculas ou minúsculas
print("limao" not in frutas) #limão não está presente?
