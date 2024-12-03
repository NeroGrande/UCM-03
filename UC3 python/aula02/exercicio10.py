print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                          ("Exercício 10:  Simulador de Conta de Energia")

#Considere que o preço da tarifa de energia é R$ 0,50 por kWh. Pergunte ao usuário o consumo de energia em kWh e 
# calcule o valor total a ser pago pela conta. Se o consumo for maior que 200 kWh, aplique um desconto de 10%.



# Preço da tarifa de energia por kWh
preco_por_kwh = 0.50

# Solicita ao usuário o consumo de energia em kWh
consumo = float(input("Digite o consumo de energia em kWh: "))

# Calcula o valor total sem desconto
valor_total = consumo * preco_por_kwh

# Aplica o desconto de 10% se o consumo for maior que 200 kWh
if consumo > 200:
    valor_total *= 0.90

# Exibe o valor total a ser pago
print(f"O valor total a ser pago é R$ {valor_total:.2f}")

