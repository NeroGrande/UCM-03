print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")
print                                                               ("Exercício 6: Média de Números Positivos")

#Escreva um programa que receba números inteiros até que o usuário digite 0. 
#Calcule e exiba a média dos números positivos digitados.

soma = 0
contador = 0


while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    if numero > 0:
        soma += numero
        contador += 1


if contador == 0:
    print("Nenhum número positivo foi digitado.")
else:
    print(f"A média dos números positivos é: {soma / contador:.2f}")
