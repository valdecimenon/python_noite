#Exemplo de importação e exportação de arquivo CSV do Excel

import csv

#Lendo o csv
def lerCsv():
    tabela = csv.reader(open('planilha.csv', encoding='UTF8'))
    for linha in tabela:
        print(linha[0].split(';'))

#Gravar dados em csv
def gravarCsv():
    #tupla com os dados
    tabela = (('PRODUTO', 'UNIDADE', 'PREÇO UNITÁRIO', 'ESTOQUE', 'VALOR TOTAL'),
              ('Açúcar', '2 Kg', '5.59', '10', '55.90'),
              ('Biscoito', '200 Gr', '1.19', '10', '11.90')
             )

    #cria um arquivo para salvar os dados
    saida = csv.writer(open('tabela_saida.csv', 'w', newline=''))

    #escreve a tupla no arquivo de saida
    saida.writerows(tabela)


if __name__ == '__main__':
    lerCsv()
    #gravarCsv()
