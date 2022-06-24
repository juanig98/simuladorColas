import math


class FinitePopulation:

    def __init__(self, arrival_rate, service_rate, num_servers, population_size):
        """"""
        # Párametros recibidos
        self.title = ' Sistema de colas (cola finita) '
        self.arrival_rate_name = 'Tasa de arribos'
        self.arrival_rate = arrival_rate  # E2
        self.service_rate_name = 'Tasa de servicio'
        self.service_rate = service_rate  # E3
        self.num_servers_name = 'Número de servidores'
        self.num_servers = num_servers  # E4
        self.population_size_name = 'Máximo tamaño de la población'
        self.population_size = population_size  # E5

        # Cálculo de valores internos
        self.__min_value = 0.0000000001
        self.__max_value = 999
        self.s_fact = math.factorial(num_servers)
        self.lambda_mu = self.arrival_rate / self.service_rate
        self._s = self.lambda_mu / self.num_servers
        self._t = (self.lambda_mu**self.num_servers) / (self.s_fact * (1-self._s))
        self.s_1 = self.num_servers - 1
        self._d = self.__calculate_d()
        self.p0 = 1/sum(self._d)
        self.pn = self.__calculate_pn()
        self._f = self.__calculate_f()
        self._f_sum = sum(self._f)
        self._g = self.__calculate_g()
        self._g_sum = sum(self._g)
        self._h = self.__calculate_h()
        self._h_sum = sum(self._h)
        self._j = self.__calculate_j()
        self._j_sum = sum(self._j)

        # Variables
        self.utilization_name = 'Utilización'
        self.utilization = self._j_sum/self.num_servers
        self.p_empty_name = 'Probabilidad de que el sistema esté vacío (P(0))'
        self.p_empty = self.p0
        self.queue_length_name = 'Clientes en la cola (Lq)'
        self.queue_length = self._f_sum
        self.number_in_system_name = "Cantidad de clientes en el sistema"
        self.number_in_system = self.queue_length + self._g_sum + self.num_servers * (1 - self._h_sum)

        self._effective_lambda = self.population_size * self.number_in_system
        self.effective_lambda = self._effective_lambda * self.arrival_rate

        self.time_in_queue_name = 'Tiempo en la cola (Wq)'
        self.time_in_queue = self.queue_length/self.effective_lambda
        self.time_in_system_name = 'Tiempo en el sistema (Wq)'
        self.time_in_system = self.number_in_system/self.effective_lambda
        self.p_customer_waits_name = 'Probabilidad que un cliente tenga que esperar'
        self.p_customer_waits = self._h_sum

    def __calculate_j(self,):
        """"""
        j = []
        for n in range(len(self.pn)):
            if n > self.num_servers:
                j.append(self.num_servers*self.pn[n])
            else:
                j.append(n*self.pn[n])
        return j

    def __calculate_h(self,):
        """"""
        g = []
        n = 0
        while n < self.num_servers:
            g.append(self.pn[n])
            n += 1
        return g

    def __calculate_g(self,):
        """"""
        g = [0]
        n = 1
        a = 1
        while a != 0:
            a = (n + 1) - self.num_servers
            g.append(n*self.pn[n])
            n += 1
        return g

    def __calculate_f(self,):
        """"""
        f = []
        _aux = 1
        n = 0
        while _aux > self.__min_value and n < self.__max_value and n < len(self.pn):
            a = n - self.num_servers
            if a > 0:
                _aux = a * self.pn[n]
                f.append(_aux)
            else:
                f.append(0)
            n += 1
        return f

    def __calculate_pn(self,):
        """"""
        pn = [self.p0]
        _aux = 1
        n = 1
        while _aux > self.__min_value and n < self.__max_value:
            a = n - self.num_servers
            b = self.population_size-n+1
            c = n
            if a > 0:
                _aux = pn[n-1]*b*self.lambda_mu/self.num_servers
                pn.append(_aux)
            else:
                _aux = pn[n-1]*b*self.lambda_mu/c
                pn.append(_aux)
            n += 1
        return pn

    def __calculate_d(self,):
        """"""
        d = [1]
        _aux = 1
        n = 0
        while _aux > self.__min_value and n < self.__max_value:
            a = n - self.num_servers
            b = self.population_size-n
            c = n + 1

            if c == 1 or a < 0:
                _aux = d[n]*b*self.lambda_mu/c
                d.append(_aux)
            else:
                _aux = d[n]*b*self.lambda_mu/self.num_servers
                d.append(_aux)
            n += 1
        return d

    def simulate(self,):
        """"""
        return [
            self.utilization_name + ': ' + str(round(self.utilization*100, 4)) + ' %',
            self.p_empty_name + ': ' + str(round(self.p_empty, 4)),
            self.queue_length_name + ': ' + str(round(self.queue_length, 4)),
            self.number_in_system_name + ': ' + str(round(self.number_in_system, 4)),
            self.time_in_queue_name + ': ' + str(round(self.time_in_queue, 4)),
            self.time_in_system_name + ': ' + str(round(self.time_in_system, 4)),
            self.p_customer_waits_name + ': ' + str(round(self.p_customer_waits, 4)),
        ]

 