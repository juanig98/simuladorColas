import sys
from matplotlib import pyplot as plt

import numpy as np
from finite_population import FinitePopulation
from finite_queue_length import FiniteQueueLength
from mg1 import MG1
from mms import MMS


EXAMPLES_MMS = [
    MMS(1, 2, 1),
    MMS(4, 6, 1),
    MMS(20, 10, 3),
    MMS(8, 5, 2),
    MMS(16, 5, 4),
    MMS(25, 30, 1),
    MMS(100, 30, 4),
]
EXAMPLES_MG1 = [
    MG1(1, 0.5, 0.05)
]
EXAMPLES_FINITE_POPULATION = [
    FinitePopulation(0.125, 2, 10, 100),
    FinitePopulation(4, 30, 4, 25),
]
EXAMPLES_FINITE_QUEUE = [
    FiniteQueueLength(6, 5, 1, 2),
    FiniteQueueLength(26, 13.035714, 1, 0),
]


class Test:

    def __init__(self, test):
        """"""
        print("TEST".center(100, '-'))
        print("\n")
        if test == 'finite_population':
            print("Test Finite Population".center(100, " "))
            self.show(EXAMPLES_FINITE_POPULATION)
        elif test == 'finite_queue':
            print("Test Finite Queue Length".center(100, " "))
            self.show(EXAMPLES_FINITE_QUEUE)
        elif test == 'mg1':
            print("Test MG1".center(100, " "))
            self.show(EXAMPLES_MG1)
        elif test == 'mms':
            print("Test MMS".center(100, " "))
            self.show(EXAMPLES_MMS)
        else:
            print("No existe ningún test para el parámetro recibido")
        print("\n")
        print("TEST".center(100, '-'))

    def show(self, examples):
        """"""
        self.print_console(examples)

    def print_console(self, examples):
        """"""
        for example in examples:
            print("\nResultados: \n")
            for result in example.simulate():
                print(result)


if len(sys.argv) == 2:
    Test(sys.argv[1])


# mms = EXAMPLES_MMS[1]
mms = MMS(20,10,3)
co = np.arange(len(mms._c))
an = 1

fig, ax = plt.subplots()
ax.set_title('MMS')
ax.set_xlabel('Numero en el sistema')
ax.set_ylabel('Probabilidad')
ax.bar(co, mms._c, an)
plt.show()
