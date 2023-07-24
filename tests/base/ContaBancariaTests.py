from classes.base.ContaBancaria import ContaBancaria

class ContaBancariaTests(object):
    print_details = False

    def test_depositar(self):
        title = self.__class__.__name__+'.test_depositar'
        if self.print_details:
            print('Exec '+title)

        # set
        c = ContaBancaria()
        value2Test = 100
        c.depositar(value2Test)

        #assert
        assertText = 'Assert '+title
        if (c.saldo == value2Test):
            print(assertText + ' Pass [OK]')
        else:
            print(assertText + ' Failed [Fail]')

    def test_sacar(self):
        title = self.__class__.__name__+'.test_depositar'
        if self.print_details:
            print('Exec '+title)

        # set
        c = ContaBancaria()
        value2insert = 100
        value2retire = 25
        c.depositar(value2insert)
        c.sacar(value2retire)

        #assert
        assertText = 'Assert '+title
        if (c.saldo == (value2insert-value2retire)):
            print(assertText + ' Pass [OK]')
        else:
            print(assertText + ' Failed [Fail]')

    def run(self):
        self.test_depositar()
        self.test_sacar()