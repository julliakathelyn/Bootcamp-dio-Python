saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")