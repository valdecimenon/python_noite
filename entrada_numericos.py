#programa permite entrada de valores numericos
#pergunta quantos valores vou querer
#entrada_numericos.py

quant = int(input('Quantos valores?'))
valores = []

for i in range(quant):
    msg = 'Digite um valor {}: '.format(i + 1)
    valor = float(input(msg))
    valores.append(valor)


#mostrar o maior valor da lista
valores = [1,2,3]

maior = valores[0]
for valor in valores:
    if (valor > maior):
        maior = valor

print("O maior valor é ", maior)

#mostrar o menor valor da lista
menor = valores[0]
for valor in valores:
    if (valor < menor):
        menor = valor

print("O menor valor é ", menor)

#mostra a média dos valores
total = 0
for valor in valores:
    total = total + valor
    

print("Média = ", total / len(valores))
