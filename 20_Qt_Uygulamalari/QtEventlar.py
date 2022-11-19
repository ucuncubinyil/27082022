import  sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.label =  QLabel("Ekranda fareyi hareket ettir veya tıkla")

        self.setCentralWidget(self.label)


    def mouseMoveEvent(self,e):
        self.label.setText("Fare hareket ettiriliyor")

    def mousePressEvent(self, e):

        self.label.setText("Fare tıklandı")


    # def mouseReleaseEvent(self, e):
    #     self.label.setText("Mouse tuşu bırakıldı")


    def  mouseDoubleClickEvent(self, e):
        self.label.setText("Fare çift tıkladı")





app = QApplication(sys.argv)
w =  MainWindow()
w.show()
app.exec_()