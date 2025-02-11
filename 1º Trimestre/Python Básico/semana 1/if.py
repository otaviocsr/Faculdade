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