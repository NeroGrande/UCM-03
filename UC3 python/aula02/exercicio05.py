print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                               ("Exercício 5: Contar Números Pares")

#Escreva um programa que receba 10 números inteiros e conte quantos deles são pares.

contador_pares = 0


for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero % 2 == 0:
        contador_pares += 1


print(f"Você digitou {contador_pares} números pares.")
