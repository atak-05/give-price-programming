import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QVBoxLayout, QWidget
from pages.mypages import MyPage
from PyQt5.QtWidgets import *


class Login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 200)

        self.label_username = QLabel('Kullanıcı Adı:', self)
        self.label_username.move(50, 50)

        self.textbox_username = QLineEdit(self)
        self.textbox_username.move(150, 50)
        self.textbox_username.resize(100, 25)

        self.label_password = QLabel('Şifre:', self)
        self.label_password.move(50, 90)

        self.textbox_password = QLineEdit(self)
        self.textbox_password.setEchoMode(QLineEdit.Password)
        self.textbox_password.move(150, 90)
        self.textbox_password.resize(100, 25)

        self.button_login = QPushButton('Giriş', self)
        self.button_login.move(150, 130)
        self.button_login.clicked.connect(self.check_login)
        self.widget = QStackedWidget()
        self.widget.addWidget(self)
        self.show()

    def check_login(self):
        username = self.textbox_username.text()
        password = self.textbox_password.text()
        if username == 'admin' and password == '1234':
            QMessageBox.information(self, 'Başarılı', 'Giriş başarılı.')
            self.goto_main_page()
        else:
            QMessageBox.warning(self, 'Hata', 'Kullanıcı adı veya şifre hatalı.')

    def goto_main_page(self):
        main_page = MyPage()
        self.widget.addWidget(main_page)
        self.widget.setCurrentIndex(1)
        
if __name__ == '__main__':
    app = QApplication([])
    login = Login()
    app.exec_()