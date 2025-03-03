# Exercício 12: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media > 10:
    print("Nota inválida")
elif media >= 9:
    print("A")
elif media >= 7.5 and media < 9:
    print("B")
elif media >= 6 and media < 7.5:
    print("C")
elif media >= 4 and media < 6:
    print("D")
elif media <= 4 and media >= 0:
    print("E")
else:
    print("Nota inválida")