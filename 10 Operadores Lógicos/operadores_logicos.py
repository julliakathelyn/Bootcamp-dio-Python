saldo = 1000
saque = 200
limite = 100


exp = saldo >= saque and saque <= limite #se uma e outra são verdades então é verdade
print(exp)

exp = saldo >= saque or saque <= limite #se uma ou outra é verdade então é verdade 
print(exp)


exp = not 1000 > 1500 # é o inverso 
print(exp)

#and - para ser true tudo tem que ser true
#or - para ser true um tem que ser true 