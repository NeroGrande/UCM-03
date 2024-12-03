print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                              ("Exercício 3: Maior de Três Números")

#Escreva um programa que receba três números inteiros e determine qual deles é o maior.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))


if a > b and a > c:
    print("O maior número é:", a)
elif b > c:
    print("O maior número é:", b)
else:
    print("O maior número é:", c)
