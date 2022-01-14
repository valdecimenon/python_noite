class Conta:

    #contrutor da classe é chamado somente durante a criação do objeto
    def __init__(self, numero, titular, saldo,  limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo +=  valor

    def sacar(self, valor):
        if (self.__saldo + self.__limite >= valor):
            self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def extrato(self):
        print(f'Saldo de R$ {self.__saldo:.2f}  Limite de R$ {self.__limite:.2f} do titular {self.__titular}')

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


if __name__ == '__main__':
    contaZe = Conta(123, 'José da Silva', 100, 1000)
    contaMaria = Conta(456, 'Maria', 100, 1000)

    contaZe.transferir(90, contaMaria)
    contaZe.limite = 5000
    contaZe.extrato()
    contaMaria.extrato()








