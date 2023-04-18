from PyQt5.QtWidgets import *
# from pages_ui.sonuc_ui import Ui_Sonuc_Form
from pages_ui.sonuc_new import Ui_Form_Sonuc
class SonucPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.sonuc  = Ui_Form_Sonuc ()
        self.sonuc.setupUi(self)
        self.sonuc.button_home.clicked.connect(self.loginpage)
    def loginpage(self):
        from .anasayfa import AnapencerePage
        self.home = AnapencerePage()
        self.close()
        self.home.show()
        print("login page")
        
        