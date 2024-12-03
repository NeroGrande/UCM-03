print                                                              ("BEM VINDO LENDA VIVA")
print                                                        ("---------------------------------")

print                                                          ("Exercício 11: Aposentadoria")

#Crie um programa que calcule o tempo restante até a aposentadoria de uma pessoa.
#Pergunte a idade e o tempo de contribuição (em anos). A pessoa pode se aposentar com 35 anos de contribuição ou 
#60 anos de idade. Mostre o tempo restante para a aposentadoria.


idade = int(input("Qual a sua idade? "))
contribuicao = int(input("Quantos anos de contribuição? "))


if contribuicao >= 35 or idade >= 60:
    print("Você já pode se aposentar.")
else:
    tempo_faltando = max(35 - contribuicao, 60 - idade)
    print(f"Você ainda precisa de {tempo_faltando} anos para se aposentar.")