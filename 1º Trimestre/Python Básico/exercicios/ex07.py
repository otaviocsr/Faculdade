# Exercício 07: Realiza a leitura de 1 int e apresenta se ele é par ou ímpar.

input = int(input("Digite um número inteiro: "))
if input % 2 == 0:
    print(f"O número {input} é par.")
else:
    print(f"O número {input} é ímpar.")