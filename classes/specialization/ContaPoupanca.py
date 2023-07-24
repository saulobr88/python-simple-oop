from classes.base.ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    rentabilidade_total = .6

    def _consulta_rentabilidade(self):
        return self.rentabilidade_total

    def rentabilidade(self):
        rent = self._consulta_rentabilidade()

        if rent < .5:
            print('Consulte o seu gerente')
        else:
            print(rent)

    def depositar(self, valor):
        self.saldo += valor
        if self.saldo >= 1000:
            self.rentabilidade_total += .1
            print('Parabéns a sua rentabilidade aumentou para %4.2f' %
                  self.rentabilidade_total)
        self.printSaldo()
