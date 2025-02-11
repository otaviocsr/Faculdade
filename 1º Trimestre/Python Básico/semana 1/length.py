nome = input("Digite seu nome: ")

tamanho = len(nome)

print("-" * 30)
print("Seu nome tem", tamanho, "caracteres")
print("-" * 30)
print("Maiúsculo:", nome.upper())
print("-" * 30)
print("Minúsculo:",nome.lower())
print("-" * 30)
print("Primeira letra maiúscula:",nome.capitalize())

print("-" * 30)
print(nome.replace("a", "4"))