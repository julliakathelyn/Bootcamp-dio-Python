#declarando funções

def exibir_mensagem():
    print("Ola Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem Vindo {nome}!")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}!")
#chamando a função
exibir_mensagem()

exibir_mensagem_2(nome = "Jullia")

exibir_mensagem_3()

exibir_mensagem_3(nome = "Kathelyn")
