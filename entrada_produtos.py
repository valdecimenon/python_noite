#entrada_produtos
#entrada 3 produtos: nome e valor



nome1 = input('Nome do produto 1: ')
valor1 = float(input('Valor do produto 1: '))

nome2 = input('Nome do produto 2: ')
valor2 = float(input('Valor do produto 2: '))

nome3 = input('Nome do produto 3: ')
valor3 = float(input('Valor do produto 3: '))

total = valor1 + valor2 + valor3
media = total / 3

print("Valor total = {}".format(total))
print("Preço médio = {}".format(media))
