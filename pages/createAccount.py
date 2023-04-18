        
from PyQt5.QtWidgets import *
# from pages_ui.sonuc_ui import Ui_Sonuc_Form
from pages_ui.create_user import Ui_Form_Create_User
class CreateAccount(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.create  = Ui_Form_Create_User ()
        self.create.setupUi(self)
        self.create.pushButton_create.clicked.connect(self.loginpage)
    def loginpage(self):
        from .login import LoginPage
        self.login = LoginPage()
        self.save_user()
        self.login.show()
        self.close()
        print("login page")
        
    def save_user(self):
        users = {}
        
        # Yeni kullanıcının id numarasını hesapla
        counter = len(users)
        user_id = counter + 1

        # Yeni kullanıcı sözlüğünü oluştur
        user_dict = {}
        user_dict["username"] = self.create.lineEdit_username.text()
        user_dict["password"] = self.create.lineEdit_2_password.text()

        # Ana sözlüğe yeni kullanıcıyı ekle
        users[user_id] = user_dict

        # Kullanıcı bilgilerini dosyaya kaydet
        with open("Kayit.txt", "a") as file:
            
                file.write(f"Id: {user_id}\n")
                file.write(f"Kullanici adi: {user_dict['username']}\n")
                file.write(f"Sifre: {user_dict['password']}\n")
                    