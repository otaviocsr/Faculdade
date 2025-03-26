# Exercício 11

""" 

• As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

• Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    • Salários até R$ 280,00 (incluindo) : aumento de 20%
    • Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    • Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    • Salários de R$ 1500,00 em diante : aumento de 5%

• Após o aumento ser realizado, informe na tela:

    • O salário antes do reajuste;
    • O percentual de aumento aplicado;
    • O valor do aumento;
    • O novo salário, após o aumento.

"""

salario = float(input("Digite o salário do colaborador: "))

print("-" * 30)

if salario <= 280:
    salario_novo = salario * 1.20
elif salario > 280 and salario <= 700:
    salario_novo = salario * 1.15
elif salario > 700 and salario <= 1500:
    salario_novo = salario * 1.10
else:
    salario_novo = salario * 1.05


print(f"Salário antigo: R${salario:.2f}")
print(f"Percentual de aumento: {salario_novo/salario:.0%}")
print(f"Valor do aumento: R${salario_novo - salario:.2f}")
print(f"Salário novo: R${salario_novo:.2f}")

