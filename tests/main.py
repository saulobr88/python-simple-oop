from tests.base.ContaBancariaTests import ContaBancariaTests
from tests.specialization.ContaPoupancaTests import ContaPoupancaTests
from tests.specialization.ContaCorrenteTests import ContaCorrenteTests

def main():
    cbt = ContaBancariaTests()
    cbt.run()

    cpt = ContaPoupancaTests()
    cpt.run()

    cct = ContaCorrenteTests()
    cct.run()

print('Exec tests.main '+' __name__='+__name__)
main()