from PyQt5.QtWidgets import *
from pages_ui.sonuc_ui import Ui_Sonuc_Form


class SonucPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.sonuc  = Ui_Sonuc_Form ()
        self.sonuc.setupUi(self)
       
