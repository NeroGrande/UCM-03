print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                              ("Exercício 2: Soma de Números Positivos")

#Escreva um programa que receba números inteiros do usuário até que um número negativo seja digitado. 
#Exiba a soma de todos os números positivos digitados.

soma = 0
while True:
    numero = int(input("Digite um número inteiro (ou um negativo para sair): "))
    if numero < 0:
        break
    soma += numero
print("A soma dos números positivos é:", soma)
