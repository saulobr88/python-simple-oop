from classes.specialization.ContaCorrente import ContaCorrente

class ContaCorrenteTests(object):
    print_details = False

    def test_depositar(self):
        title = self.__class__.__name__+'.test_depositar'
        if self.print_details:
            print('Exec '+title)

        # set
        c = ContaCorrente()
        value2Test = 100
        c.depositar(value2Test)

        #assert
        assertText = 'Assert '+title
        if (c.saldo == value2Test):
            print(assertText + ' Pass [OK]')
        else:
            print(assertText + ' Failed [Fail]')
    
    def test_depositar_com_erro(self):
        title = self.__class__.__name__+'.test_depositar_com_erro'
        if self.print_details:
            print('Exec '+title)

        # set
        c = ContaCorrente()
        value2Test = 99
        try:
            c.depositar(value2Test)
        except Exception as err:
            if self.print_details:
                print('Conta corrente não deixa depositar menos que do R$ 100,00')

        #assert
        assertText = 'Assert '+title
        if (c.saldo == 0):
            print(assertText + ' Pass [OK]')
        else:
            print(assertText + ' Failed [Fail]')

    def run(self):
        self.test_depositar()
        self.test_depositar_com_erro()
