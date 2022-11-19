import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Python QT Sinyal")

        button =  QPushButton("TIKLA BANA !")
        button.setChecked(True)
        button.clicked.connect(self.button_tiklama)


        self.label = QLabel()

        self.input =  QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout =  QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        widget =  QWidget()
        widget.setLayout(layout)


        self.setCentralWidget(widget)


    def button_tiklama(self):
        print("Tıklandı")
        self.setWindowTitle("Tıklandı")



app = QApplication(sys.argv)
w =  MainWindow()
w.show()
app.exec_()