
class MM1():

    def __init__(self, service_rate, arrival_rate):
        self.title = ' Sistema de colas M/M/1 '
        self.service_name = "Tasa de servicio"
        self.service = service_rate
        self.arrivals_name = "Tasa de arribos"
        self.arrivals = arrival_rate
        self.infinite = (self.service - self.arrivals) > 0
        self.l_name = 'Clientes en el sistema (L)'
        self.l_value = self.arrivals / (self.service-self.arrivals) if self.infinite else 0
        self.w_name = "Tiempo en el sistema (W) (en horas)"
        self.w_value = 1 / (self.service - self.arrivals) if self.infinite else 0
        self.w_name_minutes = "Tiempo en el sistema (W) (en minutos)"
        self.w_value_minutes = self.w_value*60
        self.lq_name = "Clientes en la cola (Lq)"
        self.lq_value = self.l_value*self.arrivals / self.service if self.service > 0 else 0
        self.wq_name = "Tiempo en la cola (Wq) (en horas)"
        self.wq_value = self.w_value*self.arrivals / self.service if self.service > 0 else 0
        self.wq_name_minutes = "Tiempo en la cola (Wq) (en minutos)"
        self.wq_value_minutes = self.wq_value*60

    def simulate(self):
        """ Simula la cola con los parámetros recibidos """
        return [ 
            self.arrivals_name + ': ' + str(self.arrivals),
            self.service_name + ': ' + str(self.service),
            self.l_name + ': ' + str(self.l_value),
            self.w_name + ': ' + str(self.w_value),
            self.w_name_minutes + ': ' + str(self.w_value_minutes),
            self.lq_name + ': ' + str(self.lq_value),
            self.wq_name + ': ' + str(self.wq_value),
            self.wq_name_minutes + ': ' + str(self.wq_value_minutes),
        ]