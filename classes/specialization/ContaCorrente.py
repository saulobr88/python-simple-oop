from classes.base.ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        if valor < 100:
            raise Exception(
                'Valor mínimo para deposito em conta corrente é R$ 100,00')
        else:
            super().depositar(valor)
