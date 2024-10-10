texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")
else:
    print() #ADICIONA UMA QUEBRA DE LINHA  
    print("executa no final do laço")        


 #built-in range    
for numero in range(0, 51, 5):
    print(numero, end = " ")     