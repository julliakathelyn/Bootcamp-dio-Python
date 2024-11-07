#vai retornar uma lista igual mas nao vai ser a a mesma lista

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))#prova
