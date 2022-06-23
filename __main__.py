import sys
import time
from gui.app import *
from PyQt5 import uic
from PyQt5.QtGui import QValidator, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication
from mg1 import MG1
from mm1 import MM1
from mms import MMS


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/app.ui", self)
        self.btn_simulate_mms.clicked.connect(self.simulate_mms)
        self.btn_simulate_mm1.clicked.connect(self.simulate_mm1)
        self.btn_simulate_mg1.clicked.connect(self.simulate_mg1)
        intValidator = QIntValidator(1, 9999, self)
        self.input_arrival_rate_mms.setValidator(intValidator)
        self.input_service_rate_mms.setValidator(intValidator)
        self.input_num_servers_mms.setValidator(intValidator)
        self.input_arrival_rate_mm1.setValidator(intValidator)
        self.input_service_rate_mm1.setValidator(intValidator)
        # self.hideQFrame(self.frame_results)

    def simulate_mg1(self):
        self.run(self.progress_bar_mg1)
        self.frame_results.setEnabled(True)
        try:
            arrival_rate = float(self.input_arrival_rate_mg1.text())
            average_service_time = float(self.input_average_service_time_mg1.text())
            standard_dev = float(self.input_standard_dev_mg1.text())
            mg1 = MG1(arrival_rate, average_service_time, standard_dev)
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
            results = mm1.simulate()
            self.list_results.addItem(mm1.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))

    def simulate_mms(self):
        self.run(self.progress_bar_mms)
        self.frame_results.setEnabled(True)

        try:
            service_rate = int(self.input_service_rate_mms.text())
            arrival_rate = int(self.input_arrival_rate_mms.text())
            num_servers = int(self.input_num_servers_mms.text())
            mms = MMS(service_rate, arrival_rate, num_servers)
            results = mms.simulate()
            self.list_results.addItem(mms.title.center(84, '-') + '\n',)
            self.list_results.addItems(results)
            self.list_results.addItem('\n' + "".center(96, '-') + '\n',)
            self.label_results.setText("Todo ok")
        except Exception as e:
            self.label_results.setText("Ocurrió un error.\n {}".format(str(e)))

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
