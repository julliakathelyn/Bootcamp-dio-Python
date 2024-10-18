#[ponto de inicio : ponto final]

lista = ["p", "y", "t", "h", "o", "n"]
#quer ir até o final
print(lista[2:])  # ["t", "h", "o", "n"]
#final
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]


#0:3:2 o 3 seria o ponto de parada
print(lista[0:3:2])  # ["p", "t"]

#retorna copia exata
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

#inverte
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]