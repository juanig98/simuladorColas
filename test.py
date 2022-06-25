import sys
from finite_population import FinitePopulation
from finite_queue_length import FiniteQueueLength
from mg1 import MG1
from mms import MMS


class Test:

    def __init__(self, test):
        """"""
        print("TEST".center(100, '-'))
        print("\n")
        if test == 'finite_population':
            print("Test Finite Population".center(100, " "))
            self.finite_population()
        elif test == 'finite_queue':
            print("Test Finite Queue Length".center(100, " "))
            self.finite_queue()
        elif test == 'mg1':
            print("Test MG1".center(100, " "))
            self.mg1()
        elif test == 'mms':
            print("Test MMS".center(100, " "))
            self.mms()
        else:
            print("No existe ningún test para el parámetro recibido")
        print("\n")
        print("TEST".center(100, '-'))

    def finite_population(self,):
        """"""
        examples = [
            FinitePopulation(0.125, 2, 10, 100),
            FinitePopulation(4, 30, 4, 25),
        ]
        self.print_console(examples)

    def finite_queue(self,):
        """"""
        examples = [
            FiniteQueueLength(6, 5, 1, 2),
            FiniteQueueLength(26, 13.035714, 1, 0),
        ]
        self.print_console(examples)

    def mms(self,):
        """"""
        examples = [
            MMS(1, 2, 1),
            MMS(4, 6, 1),
            MMS(20, 10, 3),
            MMS(8, 5, 2),
            MMS(16, 5, 4),
            MMS(25, 30, 1),
            MMS(100, 30, 4),
        ]
        self.print_console(examples)

    def mg1(self,):
        """"""
        examples = [
            MG1(1, 0.5, 0.05)
        ]
        self.print_console(examples)

    def print_console(self, examples):
        """"""
        for example in examples:
            print("\nResultados: \n")
            for result in example.simulate():
                print(result)

if len(sys.argv) == 2:
    Test(sys.argv[1])
