def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-Feira, 04 de Outubro de 2022",
    "Zen pf Python",
    "Beautiful is better than ugly",
    autor="Tim Peters",
    ano=1999,)    