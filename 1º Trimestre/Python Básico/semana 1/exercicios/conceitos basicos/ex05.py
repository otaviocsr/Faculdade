# Exercício 05: Realiza a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%.

input = float(input("Digite o valor do produto: "))
discount_10 = input * 0.9
discount_20 = input * 0.8
discount_50 = input * 0.5

print(f"O valor do produto com 10% de desconto é {discount_10}")
print(f"O valor do produto com 20% de desconto é {discount_20}")
print(f"O valor do produto com 50% de desconto é {discount_50}")