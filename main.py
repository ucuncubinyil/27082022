from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from registerui import Ui_MainWindow
from User import *


class Main(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.kullanici_kaydet_button.clicked.connect(self.user_register)

    def user_register(self):
        name = self.ui.kullanici_ad.text()
        surname = self.ui.kullanici_soyad.text()
        year = self.ui.kullanici_yas.text()
        job = self.ui.kullanici_meslek_combo_box.currentText()
        user = User(name=name, surname=surname, year=year, job=job)

        status = create_user(name, surname, year, job)

        if status:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Kullanıcı eklendi ")
            msg.setWindowTitle("Bilgi")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()

        self.ui.kullanici_ad.clear()
        self.ui.kullanici_soyad.clear()
        self.ui.kullanici_yas.clear()
        self.ui.kullanici_meslek_combo_box.clear()


app = QApplication([])
arayuz = Main()
arayuz.show()

app.exec_()
