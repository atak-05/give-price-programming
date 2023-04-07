from PyQt5.QtWidgets import *
from productColor import Ui_MainWindow

class productColor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.color = Ui_MainWindow()
        self.color.setupUi(self)