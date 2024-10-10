
while True:
    numero = int(input("Informe um numero"))
    
    if numero == 10:
        break

    print(numero)

#vai pular o 12 pois vai continuar o loop
for numero in range(100):

    if numero == 12:
        continue
    print(numero, end=" ")
# pula os pares
for numero in range(100):

    if numero % 2 == 0:
        continue
    print(numero, end=" ")    
    
#break para e o continue pula