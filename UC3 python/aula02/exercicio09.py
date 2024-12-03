print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                               ("Exercício 9: Contagem de Parcelas")

#Crie um programa que calcule o valor total de uma compra feita em várias parcelas. 
#Pergunte ao usuário quantas parcelas ele deseja e o valor de cada uma. 
#Se o total ultrapassar R$ 1.000,00,acrescente 5% de juros.




def calcular_total_compras():
    try:
        num_parcelas = int(input("Digite o número de parcelas: "))
        if num_parcelas <= 0:
            print("O número de parcelas deve ser maior que zero.")
            return
        
        valores_parcelas = []
        for i in range(num_parcelas):
            try:
                valor = float(input(f"Digite o valor da parcela {i+1}: R$ "))
                if valor < 0:
                    print("O valor da parcela não pode ser negativo. Tente novamente.")
                    return
                valores_parcelas.append(valor)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                return

        total = sum(valores_parcelas)
        print(f"Total inicial da compra: R$ {total:.2f}")

        if total > 1000:
            total_com_juros = total * 1.05
            print("O valor total excede R$ 1.000,00. Acrescentando 5% de juros.")
            print(f"Valor total com juros: R$ {total_com_juros:.2f}")
        else:
            print("O valor total não excede R$ 1.000,00. Nenhum juros será aplicado.")

    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro para as parcelas.")

# Executar o programa
calcular_total_compras()
