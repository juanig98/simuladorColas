import math


class FiniteQueueLength:

    def __init__(self, arrivals_rate, service_rate, num_servers, max_queue_length):
        """"""
        # Párametros recibidos
        self.title = ' Sistema de colas (cola finita) '
        self.arrivals_rate = arrivals_rate  # E2
        self.arrivals_rate_name = 'Tasa de arribos'
        self.service_rate = service_rate  # E3
        self.service_rate_name = 'Tasa de servicio'
        self.num_servers = num_servers  # E4
        self.num_servers_name = 'Número de servidores'
        self.max_queue_length = max_queue_length  # E5
        self.max_queue_length_name = 'Máximo tamaño de la cola'

        # Cálculo de valores internos
        self.__min_value = 0.0000000001
        self.__iter = 9999
        self.s_fact = math.factorial(num_servers)
        self.lambda_mu = self.arrivals_rate / self.service_rate  # B5
        self._s = self.lambda_mu / self.num_servers  # B6
        self._t = (self.lambda_mu**self.num_servers) / self.s_fact  # B7
        self._u = self.max_queue_length + self.num_servers  # D5

        self._b = self.__calculate_b()
        self._d = self.__calculate_d()
        self.p0 = self.__calculate_p0()
        self.pn = self.__calculate_pn()
        # self._f = self.__calculate_f()
        # self._g = self.__calculate_g()
        # self.comp_of_lq =

        # Variables
        # self.utilization_name = 'Utilización'
        # self.utilization = self.arrivals_rate / self.average_service_rate
        # self.p_empty_name = 'Probabilidad de sistema vacío (P(0))'
        # self.p_empty = 1 - self.utilization
        # self.queue_length_name = 'Clientes en la cola (Lq)'
        # self.queue_length = ((self.arrivals_rate**2)*(self.standard_dev**2)+(self.utilization**2))/(2*(1-self.utilization))
        # self.time_in_system_name = 'Tiempo en el sistema (Wq)'
        # self.time_in_system = self.utilization + self.queue_length
        # self.time_in_queue_name = 'Tiempo en la cola (Wq)'
        # self.time_in_queue = self.queue_length / self.arrivals_rate
        # self.p_waits_name = 'Probabilidad que un cliente tenga que esperar'
        # self.p_waits = self.average_service_time + self.time_in_queue
        # self.p_customer_balks_name = 'Probabilidad de que el cliente se vaya'
        # self.p_customer_balks = self.average_service_time + self.time_in_queue

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
        print("\n\n")
        print(self._b)
        print(self._d)
        print(self._t)
        print("\n\n")
        return 1 / (sum(self._b)+self._t * sum(self._d))

    def __calculate_f(self,):
        """"""
        f = []
        _aux = 1
        i = 0
        while _aux < self.__min_value:
            i += 1
            if i == 1:
                f.append()

    def __calculate_pn(self,):
        """"""
        d = []
        for i in range(self._u+1):
            if i < self.num_servers:
                d.append(self.lambda_mu*self.p0)

    def simulate(self,):
        """"""


# for n in range(3):
#     print(str(n))
finit_q_length = FiniteQueueLength(6, 5, 2, 4)
print(str(finit_q_length._b))
print(str(finit_q_length._d))
print(str(finit_q_length.p0))
