idade = int(input('Digite sua idade: '))

if idade <= 0:
    print('Nem nasceu ainda')
elif idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')




# if aninhado

numero = 10

if numero >= 0:
    print("Entrou no if 1")

    if numero == 0:
        print("O número é zero")
    else:
        print("O número é positivo e diferente de zero")

else:
    print("O número é negativo")