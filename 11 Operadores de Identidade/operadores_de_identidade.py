curso = "Curso de python"
nome_curso = curso
saldo, limite = 200, 200

resp = curso is nome_curso # obj a é"is" obj b?
print(resp)

resp = curso is not nome_curso# obj a não é "is not" obj b?
print(resp)

resp = saldo is limite # obj a é "is" obj b?
print(resp)