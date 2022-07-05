import math
from matplotlib import pyplot as plt

import numpy as np


class FiniteQueueLength:

    def __init__(self, arrival_rate, service_rate, num_servers, max_queue_length):
        """"""
        # Párametros recibidos
        self.title = ' Sistema de colas (cola finita) '
        self.arrival_rate = arrival_rate  # E2
        self.arrival_rate_name = 'Tasa de arribos'
        self.service_rate = service_rate  # E3
        self.service_rate_name = 'Tasa de servicio'
        self.num_servers = num_servers  # E4
        self.num_servers_name = 'Número de servidores'
        self.max_queue_length = max_queue_length  # E5
        self.max_queue_length_name = 'Máximo tamaño de la cola'

        # Cálculo de valores internos
        self.__min_value = 0.0000001
        self.__max_value = 999
        self.s_fact = math.factorial(num_servers)
        self.lambda_mu = self.arrival_rate / self.service_rate  # B5
        self._s = self.lambda_mu / self.num_servers  # B6
        self._t = (self.lambda_mu**self.num_servers) / self.s_fact  # B7
        self._u = self.max_queue_length + self.num_servers  # D5

        self._b = self.__calculate_b()
        self._d = self.__calculate_d()
        self.p0 = self.__calculate_p0()
        self._f = self.__calculate_f()
        self._g = self.__calculate_g()
        self._f_sum = sum(self._f[self._u:len(self._f)])
        self._g_sum = sum(self._g[self._u:len(self._g)])
        self.pn = self.__calculate_pn()
        self._h = self.__calculate_h()
        self._i = self.__calculate_i()
        self._h_sum = sum(self._h)
        self._i_sum = sum(self._i)

        # Variables
        self.p_empty_name = 'Probabilidad de sistema vacío (P(0))'
        self.p_empty = self.p0
        self.number_in_system_name = "Cantidad de clientes en el sistema"
        self.number_in_system = self.__calculate_l()
        self.queue_length_name = 'Clientes en la cola (Lq)'
        self.queue_length = self.number_in_system - self._i_sum - self.num_servers * (1 - self._h_sum)
        self.utilization_name = 'Utilización'
        self.utilization = (self.number_in_system - self.queue_length) / self.num_servers
        self.p_customer_balks_name = 'Probabilidad de que el cliente se vaya'
        self.p_customer_balks = self.pn[self._u]
        self.time_in_queue_name = 'Tiempo en la cola (Wq)'
        self.time_in_queue = self.queue_length/(self.arrival_rate*(1-self.p_customer_balks))
        self.time_in_system_name = 'Tiempo en el sistema (Wq)'
        self.time_in_system = self.time_in_queue + 1 / self.service_rate
        self.p_customer_waits_name = 'Probabilidad que un cliente tenga que esperar'
        self.p_customer_waits = 0 if self.max_queue_length == 0 else 1 - self._h_sum

    def __calculate_l(self,):
        """"""
        l = 0
        for i in range(len(self.pn)):
            l += i * self.pn[i]
        return l

    def __calculate_b(self,):
        """"""
        b = [1]
        for i in range(self.num_servers):
            n = i+1
            b.append(b[n-1] * self.lambda_mu / n)

        return b

    def __calculate_d(self,):
        """"""
        c = []
        for i in range(self.max_queue_length):
            n = i + 1 + self.num_servers
            c.append(self._s**(n-self.num_servers))

        return c

    def __calculate_p0(self,):
        """"""
        return 1 / (sum(self._b)+self._t * sum(self._d))

    def __calculate_f(self,):
        """"""
        f = []
        _aux = 1
        i = 0
        while _aux > self.__min_value and i < self.__max_value:
            i += 1
            if i == 1:
                f.append(self.lambda_mu*self.p0)
            else:
                _aux = f[i-2]*self.lambda_mu/i
                f.append(_aux)

        return f

    def __calculate_g(self,):
        """"""
        g = []
        _aux = 1
        i = 0
        while _aux > self.__min_value and i < self.__max_value:
            i += 1
            _aux = (self.p0 * self.lambda_mu**i) / (self.s_fact*self.num_servers**(i-self.num_servers))
            g.append(_aux)

        return g

    def __calculate_pn(self,):
        """"""
        pn = []
        for i in range(self._u+1):
            if i == 0:
                pn.append(self.p0)
            elif i < self.num_servers:
                pn.append(self._f[i-1])
            else:
                pn.append(self._g[i-1])

        return pn

    def __calculate_h(self,):
        """"""
        h = []
        for i in range(self.num_servers):
            h.append(self.pn[i])
        return h

    def __calculate_i(self,):
        """"""
        i = []
        for n in range(self.num_servers):
            i.append(self.pn[n]*n)
        return i

    def simulate(self,):
        """ Muestra los resultados de simular la cola de fila finita con los parámetros recibidos """
        return [
            str(self.utilization_name) + ': ' + str(round(self.utilization*100, 4)) + ' %',
            str(self.p_empty_name) + ': ' + str(round(self.p_empty, 4)),
            str(self.queue_length_name) + ': ' + str(round(self.queue_length, 4)),
            str(self.number_in_system_name) + ': ' + str(round(self.number_in_system, 4)),
            str(self.time_in_queue_name) + ': ' + str(round(self.time_in_queue, 4)),
            str(self.time_in_system_name) + ': ' + str(round(self.time_in_system, 4)),
            str(self.p_customer_waits_name) + ': ' + str(round(self.p_customer_waits, 4)),
            str(self.p_customer_balks_name) + ': ' + str(round(self.p_customer_balks, 4)),
        ]

    def view_graphics(self,):
        """ Muestra los gráficos de probabilidad """
        co = np.arange(len(self.pn))
        an = 1
        fig, ax = plt.subplots()
        ax.set_title(self.title)
        ax.set_xlabel('Numero en el sistema')
        ax.set_ylabel('Probabilidad')
        ax.bar(co, self.pn, an)
        plt.show()
