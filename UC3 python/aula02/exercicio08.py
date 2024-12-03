print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                               ("Exercício 8 : Cálculo IRPF")


#Escreva um programa para ler o salário de um funcionário, e calcular o IRPF que precisa ser descontado do salário
# 1 No Brasil, a tabela do Imposto de Renda para pessoas físicas (IRPF) é progressiva, ou seja, as alíquotas aumentam conforme a renda do contribuinte. A tabela é ajustada anualmente e varia de acordo com a faixa de salário. Para o ano de 2024, as faixas de tributação do Imposto de Renda para pessoas físicas são as seguintes:
# 2 Até R$ 2.112,00: isento (não paga imposto de renda)
# 3 De R$ 2.112,01 até R$ 2.826,65: 7,5% (aplica-se sobre o valor que exceder a R$ 2.112,00)
# 4 De R$ 2.826,66 até R$ 3.751,05: 15% (aplica-se sobre o valor que exceder a R$ 2.826,65)
# 5 De R$ 3.751,06 até R$ 4.664,68: 22,5% (aplica-se sobre o valor que exceder a R$ 3.751,05)
# 6 Acima de R$ 4.664,68: 27,5% (aplica-se sobre o valor que exceder a R$ 4.664,68)


def calcular_irpf(salario):
    # Faixas de salário e respectivas alíquotas
    faixas = [
        (2112.00, 0.0),        # Até R$ 2.112,00: isento
        (2826.65, 0.075),      # De R$ 2.112,01 até R$ 2.826,65: 7,5%
        (3751.05, 0.15),       # De R$ 2.826,66 até R$ 3.751,05: 15%
        (4664.68, 0.225),      # De R$ 3.751,06 até R$ 4.664,68: 22,5%
        (float('inf'), 0.275)  # Acima de R$ 4.664,68: 27,5%
    ]

    imposto = 0.0
    base_anterior = 0.0

    for limite, aliquota in faixas:
        if salario > limite:
            imposto += (limite - base_anterior) * aliquota
            base_anterior = limite
        else:
            imposto += (salario - base_anterior) * aliquota
            break

    return imposto

# Entrada do salário
try:
    salario = float(input("Digite o salário do funcionário: R$ "))
    if salario < 0:
        print("O salário não pode ser negativo.")
    else:
        irpf = calcular_irpf(salario)
        print(f"O IRPF a ser descontado é: R$ {irpf:.2f}")
except ValueError:
    print("Entrada inválida! Por favor, insira um valor numérico.")
