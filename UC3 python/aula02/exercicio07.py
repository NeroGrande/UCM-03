print                                                                     ("BEM VINDO LENDA VIVA")
print                                                               ("---------------------------------")

print                                                               ("Exercício 7: Média salarios")

#Escreva um programa para ler o salário e o sexo de vários funcionários (defina uma cláusula para terminar a leitura)
#ao término, informar a média de salário de homens e mulheres.

# Inicializando variáveis
salario_homens = salario_mulheres = contador_homens = contador_mulheres = 0


while True:
    # Leitura do salário
    salario = float(input("Informe o salário do funcionário: R$ "))

# Leitura do sexo
    sexo = input("Informe o sexo do funcionário (M/F): ").strip().upper()
   
    # Verifica se o sexo é válido
    if sexo not in ['M', 'F']:
        print("Sexo inválido! Digite 'M' para masculino ou 'F' para feminino.")
        continue
   
    # Atualiza as variáveis conforme o sexo
    if sexo == 'M':
        salario_homens += salario
        contador_homens += 1
    elif sexo == 'F':
        salario_mulheres += salario
        contador_mulheres += 1
   
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja cadastrar mais um funcionário? (s/n): ").strip().lower()
    if continuar != 's':
        break


# Calculando as médias
if contador_homens > 0:
    media_homens = salario_homens / contador_homens
    print(f"Média de salário dos homens: R$ {media_homens:.2f}")
else:
    print("Não foram informados salários de homens.")


if contador_mulheres > 0:
    media_mulheres = salario_mulheres / contador_mulheres
    print(f"Média de salário das mulheres: R$ {media_mulheres:.2f}")
else:
    print("Não foram informados salários de mulheres.")
