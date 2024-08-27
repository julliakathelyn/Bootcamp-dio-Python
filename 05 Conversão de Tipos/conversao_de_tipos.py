print(int("3"))
print(int(1.98787324))
print(float("10"))
print(float(10.30))
print(float(100))
print(str(10.50))
print(type(str(2.50))) #vai falar o tipo da variavel

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))



preco = 10
print(preco)

#conversão do tipo int para o tipo float
preco = float(preco) #especificando que deseja que converta para um float
print(preco)



# se usarmos divisão o valor vira double direto
preco = 100
print(preco)

preco = 100/2
print(preco)

preco = 10
print(preco)
print(preco / 2) # vai fazer o valor inteiro virar float
print(preco // 2) # // mantém o valor por causa das duas barras



preco = 10.30
print(preco)

#voltou a ser inteiro
preco = int(preco) #especificando que deseja que converta para um inteiro
print(preco)


#numero para string juntar mensagem a uma variavel
preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

#erro de conversão

#preco = "python"
#print(float(preco))