# class ContaBancaria(object):
#     def __init__(self) -> None:
#         self.saldo = 0

#     def printSaldo(self):
#         print(self.saldo)

#     def depositar(self, valor):
#         self.saldo += valor
#         print('depositar da classe %s' % self.__class__.__name__)
#         self.printSaldo()

#     def sacar(self, valor):
#         self.saldo -= valor
#         self.printSaldo()


# class ContaPoupanca(ContaBancaria):
#     rentabilidade_total = .6

#     def _consulta_rentabilidade(self):
#         return self.rentabilidade_total

#     def rentabilidade(self):
#         rent = self._consulta_rentabilidade()

#         if rent < .5:
#             print('Consulte o seu gerente')
#         else:
#             print(rent)

#     def depositar(self, valor):
#         self.saldo += valor
#         if self.saldo >= 1000:
#             self.rentabilidade_total += .1
#             print('Parabéns a sua rentabilidade aumentou para %4.2f' %
#                   self.rentabilidade_total)
#         self.printSaldo()


# class ContaCorrente(ContaBancaria):
#     def depositar(self, valor):
#         if valor < 100:
#             raise Exception(
#                 'Valor mínimo para deposito em conta corrente é R$ 100,00')
#         else:
#             super().depositar(valor)

from classes.specialization.ContaPoupanca import ContaPoupanca
from classes.specialization.ContaCorrente import ContaCorrente

conta_poupanca = ContaPoupanca()
"""
conta_poupanca.rentabilidade()
conta_poupanca.depositar(1000)
conta_poupanca.rentabilidade()
conta_poupanca.sacar(50)
"""
conta_corrente = ContaCorrente()
conta_corrente.depositar(100)
