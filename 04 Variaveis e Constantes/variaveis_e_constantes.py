age = 20
name = 'Jullia'
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade.')


idade, nome = (20, "Jullia")
print(f"Meu nome é {nome} e eu tenho {idade} anos(s) de idade.")

#aqui estamos reatribuindo os valores das variaveis name e age
age = 30
name = 'Arthur'
print(f'Meu nome é {name} e eu tenho {age} anos(s) de idade.')

#boas praticas
#snake_case = todo espaço vira _ e tudo fica em minusculo

limite_saque_diario = 1000 #essa variavel esta legivel para compreenção independete do tempo que o desenvolvedor passe sem olhar esse codigo

# essas variaveis nao tem uma boa coompreenção para o desenvolvedor olhar para elas daqui anos por exemplo
lim_saq_di = 2000
a = 1200
x = 2030

 # constante é um combinado que variaveis escritas em MAIUSCULO são constantes mas na pratica se você tentar mudar o valor ele será alterado
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]
print(BRAZILIAN_STATES)