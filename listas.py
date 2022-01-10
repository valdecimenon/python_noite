#Programa listas.py

#inicializa a lista
lista = []
precos = []
estoque = []


def menu():
    print('\n\n\n\n\n######### Controle de Estoque #########')
    print('1 = Entrar estoque')
    print('2 = Imprime estoque')
    print('3 = Relatório estoque')
    print('4 = Sair do programa')

    opcao = -1
    #loop
    while (opcao < 1 or opcao > 4):
        opcao = int(input('Qual opção? '))
        if (opcao < 1 or opcao > 4):
            print('Opção inválida! Digite um valor entre 1 e 4')
    return opcao


#define função entrar estoque
def entrarEstoque():
    #converte string em inteiro
    #int('5') => 5
    quant = int(input('Quantas frutas? '))

    for i in range(quant):
        fruta = input('Digite o nome da fruta: ')
        lista.append(fruta)
        #float('1.99') => 1.99
        preco = float(input('Preço da fruta: '))
        precos.append(preco)
        num = int(input('Quantidade de frutas em estoque: '))
        estoque.append(num)

def imprimeEstoque():
    print(lista)
    print(precos)
    print(estoque)

def relatorioEstoque():
    print('------------ Relatório do Estoque ----------')
    print('Tipos de frutas no estoque: ', len(lista))
    total = 0;
    for quant in estoque:
        total = total + quant
    print('Quantidade de frutas no estoque: ', total)



#loop principal
escolha = 0
while (escolha != 4):
    escolha = menu()

    if (escolha == 1):
        entrarEstoque()
        
    elif (escolha == 2):
        imprimeEstoque()
        
    elif (escolha == 3):
        relatorioEstoque()

    else:
        print('Saindo... Adeus!')


