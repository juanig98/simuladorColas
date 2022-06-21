
import math


class MMS():

    def __init__(self, service_rate, arrival_rate, num_servers):
        self.title = ' Sistema de colas M/M/S '
        self.service_name = "Tasa de servicio"
        self.service = service_rate
        self.arrivals_name = "Tasa de arribos"
        self.arrivals = arrival_rate
        self.num_servers_name = "Número de servidores "
        self.num_servers = num_servers

        # Calculates values
        self.lambda_mu = self.arrivals / self.service
        self._s = self.lambda_mu / self.num_servers
        self.s1 = self.num_servers-1
        self.fact_s1 = math.factorial(self.s1)
        self._t = (self.lambda_mu**self.num_servers)/(self.fact_s1*self.num_servers*(1-self._s))
        self.p = self.calculateP()
        self.p0 = self.calculateP0()
        self.recalculateP()

        # Vars
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
        self.p_waits = self.calculate_pw()

    def calculate_pw(self):
        sum = 0
        for x in range(self.num_servers):
            sum += self.p[x]['d']

        return 1-sum

    def calculateP0(self):
        sum = 0
        for x in range(self.num_servers):
            sum += self.p[x]['b']

        return 1/(sum+self._t)

    def recalculateP(self):
        for x in range(self.num_servers):
            if x == 0:
                self.p[x]['c'] = self.p0
            else:
                self.p[x]['c'] = (self.p[x-1]['c']*self.lambda_mu)/self.num_servers if x > self.num_servers else (self.p[x-1]['c']*self.lambda_mu)/x

            self.p[x]['d'] = self.p[x]['c'] if x < self.num_servers else 0

    def calculateP(self):
        p = []
        for x in range(self.num_servers):
            if x == 0:
                p.append(dict(a=x, b=1, c=0, d=0))
            else:
                if x > self.s1:
                    p.append(dict(a=x, b=0, c=0, d=0))
                else:
                    if x == 1:
                        p.append(dict(a=x, b=self.lambda_mu, c=0, d=0))
                    else:
                        p.append(dict(a=x, b=p[x-1]['b']*self.lambda_mu/x, c=0, d=0))
        return p

    def graf(self):
        print('\n' + self.title.center(80, '-') + '\n')
        print('{}:\t {}'.format(str(self.arrivals_name), str(self.arrivals)))
        print('{}:\t {}'.format(str(self.service_name), str(self.service)))
        print('{}:\t {}'.format(str(self.num_servers_name), str(self.num_servers)))
        print('\n')
        print('{}:\t {}'.format(str(self.utilization_name), str(self.utilization)))
        print('{}:\t {}'.format(str(self.p_empty_name), str(self.p_empty)))
        print('{}:\t {}'.format(str(self.queue_length_name), str(self.queue_length)))
        print('{}:\t {}'.format(str(self.number_in_system_name), str(self.number_in_system)))
        print('{}:\t {}'.format(str(self.time_in_queue_name), str(self.time_in_queue)))
        print('{}:\t {}'.format(str(self.time_in_system_name), str(self.time_in_system)))
        print('{}:\t {}'.format(str(self.p_waits_name), str(self.p_waits)))
        print('\n')
