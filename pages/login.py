# import sys
from PyQt5 import QtWidgets
# from pages.mypages import MyPage
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from pages_ui.login_ui_new import Ui_Form
from .anasayfa import AnapencerePage
from .createAccount import CreateAccount
class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.loginform.pushButton_login.clicked.connect(self.check_login)
        self.createAccount = CreateAccount()
        self.loginform.button_create_user.clicked.connect(self.create_account)
        self.username = ""
        self.password = ""
        self.users = {}
        
    def check_login(self):
        
        username = self.loginform.username.text()
        password = self.loginform.password.text()
        self.users = {}
        self.file() 
        print(self.users.keys())   
        if self.users != None :     
            if username ==  'admin' or (username in self.users['Kullanici adi'] and self.users['Sifre'] == password):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("<html><b><font color='black'>Giriş Başarılı!</font></b></html>")
                msg.setWindowTitle("Başarılı")
                msg.setStyleSheet("QMessageBox { background-color: white; }")
                msg.setStyleSheet("background-color:#ecc5e9")
                msg.exec_()
                self.close()
                self.anasayfa_ac = AnapencerePage()
                self.anasayfa_ac.show()
            else:
                QMessageBox.warning(self, 'Hata', 'Kullanıcı adı veya şifre hatalı.')
        else : 
            QMessageBox.warning(self, 'Hata', 'Lütfen bir kullanıcı oluşturun!')
    def create_account(self):
        from .createAccount import CreateAccount
        self.createAccount = CreateAccount()
        self.close()
        self.createAccount.show()
        
    def file(self):
        self.users = {}
        with open("Kayit.txt", "r") as file:
            for line in file:
                split_line = line.strip().split(":")
                if len(split_line) == 2:
                    key = split_line[0].strip()
                    value = split_line[1].strip()
                    self.users[key] = value
                else:
                    continue
        print(self.users)
          
            

