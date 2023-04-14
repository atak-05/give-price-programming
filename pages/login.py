# import sys
# from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QVBoxLayout, QWidget
# from pages.mypages import MyPage
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from pages_ui.login_python import Ui_Form
from .anasayfa import AnapencerePage

class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.anasayfa_ac = AnapencerePage()
        self.loginform.pushButton.clicked.connect(self.check_login)


    def check_login(self):
        username = self.loginform.lineEdit_username.text()
        password = self.loginform.lineEdit_password.text()
        if username == '' and password == '':
            QMessageBox.information(self, 'Başarılı', 'Giriş başarılı.')
            self.close()
            self.anasayfa_ac.show()
        else:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı veya şifre hatalı.')

    