print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                                   ("Exercício 4: Tabuada")

#Escreva um programa que exiba a tabuada de multiplicação de 
#um número digitado pelo usuário, de 1 a 10.

numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")