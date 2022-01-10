#matriz.py

lista = [1, 2, 3]
print("Lista: ", lista)

#lista com sublista aninhada
lista = [1, 2, 3, "banana", 'uva', [4, 5, 6, [7, 8, 9]]]
print(lista)

print(lista[5])
print(lista[5][3][0])

#criando uma matriz a partir de listas
#uma matriz é formada por linha e coluna
#em python uma matriz é uma lista formada de sublista
#sendo que cada sublista forma uma linha da matriz
print('Matriz usando lista')
      #col  0 1 2
matriz = [ [1,2,3],  #linha 0
           [4,5,6],  #linha 1
           [7,8,9]   #linha 2
         ]

print(matriz)
print(matriz[0]) #linha 0
print(matriz[1]) #linha 1
print(matriz[2]) #linha 2

print("Linha 1, coluna 1: ", matriz[1][1])
print("Linha 2, coluna 0: ", matriz[2][0])



print("\n\nImprimindo a matriz com for:")
for linha in matriz:
    print('')
    for col in linha:
        print(f' {col}', end='')




print("\n\nMostrando os índices da matriz:")
i = 0 #número da linha na matriz (lista)

for linha in matriz:
    print('')
    j = 0 #número da coluna na matriz
    for col in linha:
        valor = matriz[i][j]
        print(f'\t{i},{j}={valor}', end='')
        j += 1

    i += 1

#Criando uma matriz através da entrada de usuário
qlinhas = int(input('\n\nQuantidade de linhas: '))
qcolunas = int(input('\nQuantidade de colunas: '))

linha = [0] * qcolunas
matriz = [linha] * qlinhas
print(matriz)

#Matriz com a bibliteca numpy
import numpy as np

print('Matriz usando numpy')
matriz = np.array(
                  [ [1,2,3],  #linha 0
                    [4,5,6],  #linha 1
                    [7,8,9]   #linha 2
                  ]      
                 )
print(matriz)



