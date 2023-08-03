# Int <> Float
preço = 10
preço = float(preço) # preço / 2 = 5.0
print(preço)         # preço // 2 = 5

valor = 10.30
valor = int(preço)
print(valor)

# Númerico <> Str
preço = 10.50
idade = 28

print(str(preço))
print(str(idade))

texto = f"idade {idade}, preço {preço}" #concatenando
print(texto)

preço_str = "10.50"
idade_str = "28"

print(float(preço_str))
print(float(idade_str))

# Erro de Conversão
preço_erro = "python"
print(float(preço_erro)) #Traceback