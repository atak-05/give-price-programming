# from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout,QDialog

# class MyPage(QDialog):
#     def __init__(self):
#         super(MyPage,self).__init__()
        
#         # QLabel nesnesi oluştur
#         label = QLabel("Bu bir örnek sayfadır.")
        
#         # QVBoxLayout nesnesi oluştur
#         layout = QVBoxLayout()
        
#         # QLabel nesnesini layout'a ekle
#         layout.addWidget(label)
        
#         # Widget'a layout'u ekle
#         self.setLayout(layout)
from PyQt5.QtWidgets import *
# from pages_ui.anasayfa_python import Ui_MainWindow
from .product import ProductPage
from pages_ui.anasayfa_new import  Ui_Form_Homepage


class AnapencerePage(QWidget):
    def __init__(self):
        super().__init__()
        self.anapencereform =  Ui_Form_Homepage()
        self.anapencereform.setupUi(self)
        self.product_ac = ProductPage()
        self.anapencereform.fiyat_al.clicked.connect(self.fiyat_al)
    def fiyat_al(self):
        self.product_ac.show()
        self.close()