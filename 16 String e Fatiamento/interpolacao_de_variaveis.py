nome = "Jullia"
idade = 20
profissao = "programadora"
linguagem = "Python"

print("Ola chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." %(nome,idade,profissao,linguagem))

#format
print("Ola chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculada no curso de {}." .format(nome,idade,profissao,linguagem))

print("Ola chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculada no curso de {0}." .format(nome,idade,profissao,linguagem))

print()
print("Ola chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}." .format(nome = nome,idade = idade ,profissao = profissao ,linguagem = linguagem))

print()
#print("Ola chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}." .format(**pessoa))

#f string

print(f"Ola chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculada no curso de {linguagem}." )

PI = 3.14159

print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")