class ContaBancaria(object):
    def __init__(self) -> None:
        self.saldo = 0

    def printSaldo(self):
        print(self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print('depositar da classe %s' % self.__class__.__name__)
        self.printSaldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.printSaldo()
