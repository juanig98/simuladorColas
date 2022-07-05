import sys
import time
from finite_population import FinitePopulation
from finite_queue_length import FiniteQueueLength
from gui.app import *
from PyQt5 import uic
from PyQt5.QtGui import QValidator, QDoubleValidator
from PyQt5.QtWidgets import QMainWindow, QApplication
from mg1 import MG1
from mm1 import MM1
from mms import MMS


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/app.ui", self)
        self.memory = None
        self.assign_events()
        self.validators()
    
    def view_graphics(self):
        try:
            self.memory.view_graphics()
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))
            
    def simulate_mms(self):
        self.run(self.progress_bar_mms)
        self.frame_results.setEnabled(True)

        try:
            service_rate = int(self.input_service_rate_mms.text())
            arrival_rate = int(self.input_arrival_rate_mms.text())
            num_servers = int(self.input_num_servers_mms.text())
            mms = MMS(arrival_rate, service_rate, num_servers)
            self.memory = mms
            results = mms.simulate()
            self.list_results.addItem(mms.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.btn_view_images_mms.setEnabled(True)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))
                        
    def simulate_finite_q_length(self):
        self.run(self.progress_bar_finite_q_length)
        self.frame_results.setEnabled(True)

        try:
            service_rate = int(self.input_service_rate_finite_q_length.text())
            arrival_rate = int(self.input_arrival_rate_finite_q_length.text())
            num_servers = int(self.input_num_servers_finite_q_length.text())
            max_queue_length = int(self.input_max_queue_length_finite_q_length.text())
            fql = FiniteQueueLength(arrival_rate, service_rate, num_servers, max_queue_length)
            self.memory = fql
            results = fql.simulate()
            self.list_results.addItem(fql.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.btn_view_images_finite_q_length.setEnabled(True)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))
            
    def simulate_finite_population(self):
        """"""
        self.run(self.progress_bar_finite_q_length)
        self.frame_results.setEnabled(True)

        try:
            service_rate = int(self.input_service_rate_finite_population.text())
            arrival_rate = int(self.input_arrival_rate_finite_population.text())
            num_servers = int(self.input_num_servers_finite_population.text())
            population_size = int(self.input_population_size_finite_population.text())
            fp = FinitePopulation(arrival_rate, service_rate, num_servers, population_size) 
            self.memory = fp
            results = fp.simulate()
            self.list_results.addItem(fp.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.btn_view_images_finite_population.setEnabled(True)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))

    def simulate_mg1(self):
        self.run(self.progress_bar_mg1)
        self.frame_results.setEnabled(True)
        try:
            arrival_rate = int(self.input_arrival_rate_mg1.text())
            average_service_time = int(self.input_average_service_time_mg1.text())
            standard_dev = int(self.input_standard_dev_mg1.text())
            mg1 = MG1(arrival_rate, average_service_time, standard_dev)
            self.memory = mg1
            results = mg1.simulate()
            self.list_results.addItem(mg1.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))

    def simulate_mm1(self):
        self.run(self.progress_bar_mm1)
        self.frame_results.setEnabled(True)
        try:
            service_rate = int(self.input_service_rate_mm1.text())
            arrival_rate = int(self.input_arrival_rate_mm1.text())
            mm1 = MM1(service_rate, arrival_rate)
            self.memory = mm1
            results = mm1.simulate()
            self.list_results.addItem(mm1.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))

    def assign_events(self,):
        self.btn_simulate_mms.clicked.connect(self.simulate_mms)
        self.btn_simulate_mm1.clicked.connect(self.simulate_mm1)
        self.btn_simulate_mg1.clicked.connect(self.simulate_mg1)
        self.btn_simulate_finite_q_length.clicked.connect(self.simulate_finite_q_length)
        self.btn_simulate_finite_population.clicked.connect(self.simulate_finite_population)
        self.btn_view_images_mms.clicked.connect(self.view_graphics)
        self.btn_view_images_mms.setEnabled(False)
        self.btn_view_images_finite_q_length.clicked.connect(self.view_graphics)
        self.btn_view_images_finite_q_length.setEnabled(False)
        self.btn_view_images_finite_population.clicked.connect(self.view_graphics)
        self.btn_view_images_finite_population.setEnabled(False)
 
    def validators(self,):
        intValidator = QDoubleValidator(0, 9999, 4, self)
        self.input_arrival_rate_mms.setValidator(intValidator)
        self.input_service_rate_mms.setValidator(intValidator)
        self.input_num_servers_mms.setValidator(intValidator)
        self.input_arrival_rate_mm1.setValidator(intValidator)
        self.input_service_rate_mm1.setValidator(intValidator)
        self.input_average_service_time_mg1.setValidator(intValidator)
        self.input_arrival_rate_finite_q_length.setValidator(intValidator)
        self.input_service_rate_finite_q_length.setValidator(intValidator)
        self.input_num_servers_finite_q_length.setValidator(intValidator)
        self.input_max_queue_length_finite_q_length.setValidator(intValidator)
        self.input_arrival_rate_finite_population.setValidator(intValidator)
        self.input_service_rate_finite_population.setValidator(intValidator)
        self.input_num_servers_finite_population.setValidator(intValidator)
        self.input_population_size_finite_population.setValidator(intValidator)
        
    
    def showQFrame(self, qframe):
        QtWidgets.QFrame.show(qframe)
        return

    def hideQFrame(self, qframe):
        " Handles the hiding of the panel and markers "
        QtWidgets.QFrame.hide(qframe)
        self.__text = None
        self.__paramPositions = None
        self.__highlightedParam = None
        return

    def run(self, progress_bar):
        for i in range(100):
            time.sleep(0.005)
            progress_bar.setProperty("value", i+1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = MainApp()
    GUI.show()
    sys.exit(app.exec_())
