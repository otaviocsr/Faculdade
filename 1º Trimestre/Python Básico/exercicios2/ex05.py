# Faça um Programa que converta metros para centímetros.

def metros_para_centimetros(metros):
    return metros * 100

metros = float(input("Digite o valor em metros: "))
print(f"{metros} metros é igual a {metros_para_centimetros(metros)} centímetros.")
