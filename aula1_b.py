#Estruturas de decisão

temp = int(input('Entre com a temperatura: '))


if temp < 0:
    print('Congelando')
elif temp <= 20:
    print('Frio')
elif temp <= 25:
    print('Normal')
elif temp <= 35:
    print('Quente')
else:
    print('Muito Quente!')

print('Fim do programa')
