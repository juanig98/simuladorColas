import sys
from gui.app import *
from PyQt5 import uic
from PyQt5.QtGui import QValidator, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication
from mm1 import MM1
from mms import MMS


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/app.ui", self)
        self.btn_simulate.clicked.connect(self.simulate)
        intValidator = QIntValidator(1, 9999, self)
        # validator = QValidator()
        self.lineEdit_arrival_rate.setValidator(intValidator)
        # self.lineEdit_arrival_rate.setValidator(validator)
        self.lineEdit_service_rate.setValidator(intValidator)
        self.lineEdit_num_servers.setValidator(intValidator)
        self.hideQFrame(self.frame_results_mms)

    def simulate(self):
        service_rate = int(self.lineEdit_service_rate.text())
        arrival_rate = int(self.lineEdit_arrival_rate.text())
        num_servers = int(self.lineEdit_num_servers.text())

        mms = MMS(service_rate, arrival_rate, num_servers)
        results = mms.graf()
        self.showQFrame(self.frame_results_mms)
        self.frame_results_mms.setEnabled(True)
        
        self.list_results_mms.addItems(results)
        # for i in results:
        #     # print(i[0])
        #     self.list_results_mms.addItem(i[0])
        
    
    def showQFrame(self, qframe):
        QtWidgets.QFrame.show(qframe)
        return
    
    def hideQFrame(self, qframe):
        " Handles the hiding of the panel and markers "
        QtWidgets.QFrame.hide(qframe)
        self.__text = None
        self.__paramPositions = None
        self.__highlightedParam = None
        # self.__calltipLabel.setText("")
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = MainApp()
    GUI.show()
    sys.exit(app.exec_())

# mm1 = MM1(service_rate=2,arrival_rate=1)
# mm1.graf()
# mm1 = MM1(service_rate=6,arrival_rate=4)
# mm1.graf()

# mms = MMS(service_rate=3, arrival_rate=8, num_servers=3)
# mms = MMS(service_rate=10, arrival_rate=20, num_servers=3)
# mms = MMS(service_rate=5, arrival_rate=8, num_servers=2)
# mms = MMS(service_rate=5, arrival_rate=16, num_servers=4)
# mms.graf()
