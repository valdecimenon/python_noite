#entrada_produtos_for.py
#entrada 3 produtos: nome e valor

nomes = []
valores = []

quant = int(input('Quantos produtos? '))
total = 0

for i in range(quant):
    nome = input('Nome do produto {}: '.format(i + 1))
    valor = float(input('Valor do produto {}: '.format(i + 1)))
    total = total + valor

    nomes.append(nome)
    valores.append(valor)

print(nomes)
print(valores)

print('Total = R$ {:.2f}'.format(total))
print('Média = R$ {:.2f}'.format(total / quant))
