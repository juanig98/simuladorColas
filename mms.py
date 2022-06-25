
import math


class MMS():

    def __init__(self, arrival_rate, service_rate, num_servers):
        # Párametros recibidos
        self.title = ' Sistema de colas M/M/S '
        self.service_name = "Tasa de servicio"
        self.service = service_rate
        self.arrivals_name = "Tasa de arribos"
        self.arrivals = arrival_rate
        self.num_servers_name = "Número de servidores "
        self.num_servers = num_servers

        # Cálculo de valores internos
        self.lambda_mu = self.arrivals / self.service
        self._s = self.lambda_mu / self.num_servers
        self.s1 = self.num_servers-1
        self.fact_s1 = math.factorial(self.s1)
        self._t = (self.lambda_mu**self.num_servers)/(self.fact_s1*self.num_servers*(1-self._s))
        self.p = self.__calculate_p()
        self.p0 = self.__calculate_p0()
        self.__recalculate_p()

        # Variables
        self.utilization_name = "Utilización"
        self.utilization = self.arrivals / (self.service*self.num_servers)
        self.p_empty_name = "Probabilidad de sistema vacío (P(0))"
        self.p_empty = self.p0
        self.queue_length_name = "Clientes en la cola (Lq)"
        self.queue_length = (self.p0*(self.lambda_mu**(self.num_servers+1)))/(self.fact_s1*((self.num_servers-self.lambda_mu)**2))
        self.number_in_system_name = "Clientes en la sistema (L)"
        self.number_in_system = self.queue_length+self.lambda_mu
        self.time_in_queue_name = "Tiempo en la cola (Wq)"
        self.time_in_queue = self.queue_length/self.arrivals
        self.time_in_system_name = "Tiempo en el sistema (Wq)"
        self.time_in_system = self.time_in_queue+1/self.service
        self.p_waits_name = "Probabilidad que un cliente tenga que esperar"
        self.p_waits = self.__calculate_pw()

    def __calculate_pw(self):
        """ Cálcula el valor de la probabilidad de espera """
        sum = 0
        for n in range(self.num_servers):
            sum += self.p[n]['d']

        return 1-sum

    def __calculate_p0(self):
        """ Cálcula el valor de P(O) """
        sum = 0
        for n in range(self.num_servers):
            sum += self.p[n]['b']

        return 1/(sum+self._t)

    def __recalculate_p(self):
        """ Cálcula nuevamente el valor de P conociendo los valores de c y d"""
        for n in range(self.num_servers):
            if n == 0:
                self.p[n]['c'] = self.p0
            else:
                self.p[n]['c'] = (self.p[n-1]['c']*self.lambda_mu)/self.num_servers if n > self.num_servers else (self.p[n-1]['c']*self.lambda_mu)/n

            self.p[n]['d'] = self.p[n]['c'] if n < self.num_servers else 0

    def __calculate_p(self):
        """ Calcula el valor de P"""
        p = []
        for n in range(self.num_servers):
            if n == 0:
                p.append(dict(a=n, b=1, c=0, d=0))
            else:
                if n > self.s1:
                    p.append(dict(a=n, b=0, c=0, d=0))
                else:
                    if n == 1:
                        p.append(dict(a=n, b=self.lambda_mu, c=0, d=0))
                    else:
                        p.append(dict(a=n, b=p[n-1]['b']*self.lambda_mu/n, c=0, d=0))
        return p

    def simulate(self):
        """ Simula la cola con los parámetros recibidos """
        return [
            str(self.arrivals_name) + ': ' + str(round(self.arrivals, 3)),
            str(self.service_name) + ': ' + str(round(self.service, 3)),
            str(self.num_servers_name) + ': ' + str(round(self.num_servers, 3)),
            str(self.utilization_name) + ': ' + str(round(self.utilization*100, 3)) + ' %',
            str(self.p_empty_name) + ': ' + str(round(self.p_empty, 3)),
            str(self.queue_length_name) + ': ' + str(round(self.queue_length, 3)),
            str(self.number_in_system_name) + ': ' + str(round(self.number_in_system, 3)),
            str(self.time_in_queue_name) + ': ' + str(round(self.time_in_queue, 3)),
            str(self.time_in_system_name) + ': ' + str(round(self.time_in_system, 3)),
            str(self.p_waits_name) + ': ' + str(round(self.p_waits, 3)),
        ]
