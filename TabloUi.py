from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from pyqt5_plugins.examplebutton import QtWidgets

from showtableui import Ui_MainWindow
from User import *


class Main(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_data()




    def  set_data(self):
        self.ui.tablo.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tablo.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tablo.setAlternatingRowColors(True)

        data =  list_users()
        self.ui.tablo.setRowCount(0)

        for row_number, row_data in enumerate(data):
            self.ui.tablo.insertRow(row_number)
            for columb_number, data in enumerate(row_data):
                self.ui.tablo.setItem(row_number, columb_number, QtWidgets.QTableWidgetItem(str(data)))

app = QApplication([])
arayuz = Main()
arayuz.show()

app.exec_()
