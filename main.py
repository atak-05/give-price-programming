from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QStackedWidget, QVBoxLayout
from pages.mypages import MyPage
from PyQt5 import QtWidgets
from pages.login import Login

app = QApplication(sys.argv)
login = Login()
login.show()

sys.exit(app.exec_())
