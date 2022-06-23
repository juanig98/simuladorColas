class MG1:

    def __init__(self, arrival_rate, average_service_time, standard_dev):
        self.title = ' Sistema de colas M/G/1 '
        self.arrivals_name = 'Tasa de arribos'
        self.arrivals_rate = arrival_rate
        self.average_service_time_name = 'Tiempo promedio de servicio'
        self.average_service_time = average_service_time
        self.standard_dev_name = 'Desviación estándar del tiempo de servicio'
        self.standard_dev = standard_dev
        self.average_service_rate_name = 'Tasa de servicio promedio'
        self.average_service_rate = 1 / self.average_service_time
        self.utilization_name = 'Utilización'
        self.utilization = self.arrivals_rate / self.average_service_rate
        self.p_empty_name = 'Probabilidad de sistema vacío (P(0))'
        self.p_empty = 1 - self.utilization
        self.queue_length_name = 'Clientes en la cola (Lq)'
        self.queue_length = ((self.arrivals_rate**2)*(self.standard_dev**2)+(self.utilization**2))/(2*(1-self.utilization))
        self.time_in_system_name = 'Tiempo en el sistema (Wq)'
        self.time_in_system = self.utilization + self.queue_length
        self.time_in_queue_name = 'Tiempo en la cola (Wq)'
        self.time_in_queue = self.queue_length / self.arrivals_rate
        self.p_waits_name = 'Probabilidad que un cliente tenga que esperar'
        self.p_waits = self.average_service_time + self.time_in_queue

    def simulate(self):
        """ Simula la cola con los parámetros recibidos """
        return [
            self.arrivals_name + ': ' + str(round(self.arrivals_rate, 3)),
            self.average_service_time_name + ': ' + str(round(self.average_service_time, 3)),
            self.standard_dev_name + ': ' + str(round(self.standard_dev, 3)),
            self.average_service_rate_name + ': ' + str(round(self.average_service_rate, 3)),
            self.utilization_name + ': ' + str(round(self.utilization*100, 3)) + ' %',
            self.p_empty_name + ': ' + str(round(self.p_empty, 3)),
            self.queue_length_name + ': ' + str(round(self.queue_length, 3)),
            self.time_in_system_name + ': ' + str(round(self.time_in_system, 3)),
            self.time_in_queue_name + ': ' + str(round(self.time_in_queue, 3)),
            self.p_waits_name + ': ' + str(round(self.p_waits, 3)),
        ]
