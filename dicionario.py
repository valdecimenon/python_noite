#dicionario.py

#Dicionarios são indexados por chaves (keys)
#chave : valor
#key : value
tel = {'joao' : 1234, 'maria' : 5678}
print(tel['joao'])

#altera
tel['joao'] = 3333
print(tel['joao'])

if 'joao' in tel:
    print('existe telefone do João')

if 'beatriz' not in tel:
    print('não existe beatriz')

#retorna todas as chaves do dicionario
print('Retornando as chaves: ')
print(list(tel))

#apaga uma chave e seu valor
del tel['joao']
print(tel)
