# import sys
from PyQt5 import QtWidgets
# from pages.mypages import MyPage
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from pages_ui.login_ui_new import Ui_Form
from .anasayfa import AnapencerePage
from pages_ui.messages import Ui_Form_Message
class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.anasayfa_ac = AnapencerePage()
        self.loginform.pushButton_login.clicked.connect(self.check_login)
        self.messages = Ui_Form_Message()
    def check_login(self):
        
        username = self.loginform.username.text()
        password = self.loginform.password.text()
        if (username ==  'admin') and (password ==  '1234' ):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("<html><b><font color='black'>Giriş Başarılı!</font></b></html>")
            msg.setWindowTitle("Başarılı")
            msg.setStyleSheet("QMessageBox { background-color: white; }")
            msg.setStyleSheet("background-color:#ecc5e9")
            msg.exec_()
            self.close()
            self.anasayfa_ac.show()
        else:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı veya şifre hatalı.')
          
            

    