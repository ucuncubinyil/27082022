import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        self.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(120)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()


        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        #
        # tolbar = NavigationToolbar(sc,self)
        #
        # layout =  QtWidgets.QVBoxLayout()
        # layout.addWidget(tolbar)
        # layout.addWidget(sc)
        #
        # widget =  QtWidgets.QWidget()
        # widget.setLayout(layout)
        #
        # self.setCentralWidget(widget)
        #
        # self.show()

    def update_plot(self):
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()