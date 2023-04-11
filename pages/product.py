from PyQt5.QtWidgets import *
from pages_ui.deneme import Ui_product
from .sonuc import SonucPage
# from pages_ui.product_python import Ui_product


class ProductPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        urun_listesi = {
                    "kalem": {"renkler": {"mavi": 3, "siyah": 5, "kırmızı": 4}, "fiyat": None},
                    "defter": {"renkler": {"sarı": 8, "pembe": 10, "yeşil": 9}, "fiyat": None},
                    "kalemlik": {"renkler": {"mor": 6, "turuncu": 7, "beyaz": 8}, "fiyat": None},
                    "bardak": {"renkler": {"şeffaf": 2, "mavi": 3, "kırmızı": 4}, "fiyat": None}
                }
        self.productform = Ui_product()
        self.productform.setupUi(self,urun_listesi)
    #     self.productform.pushButton_product_type.clicked.connect(self.productColor)
    #     self.productform.pushButton_2_product_color.clicked.connect(self.productNumber)
    #     self.productform.pushButton_3_product_number.clicked.connect(self.sonuc)
    #     self.sonucform = SonucPage()
    # def productColor(self):
    #     self.productform.stackedWidget.setCurrentIndex(1)
    # def productNumber(self):
    #     self.productform.stackedWidget.setCurrentIndex(2)
    # def sonuc(self):
    #     self.sonucform.show()
    #     self.hide()
  

# class ProductPage(QWidget):
#     def __init__(self) -> None:
#         super().__init__()
#         self.productform = Ui_product()
#         self.productform.setupUi(self)
#         self.productform.pushButton_product_type.clicked.connect(self.productColor)
#         self.productform.pushButton_2_product_color.clicked.connect(self.productNumber)
#         self.productform.pushButton_3_product_number.clicked.connect(self.sonuc)
#         self.sonucform = SonucPage()
#         self.product_type = ["a","b"]
#     def productColor(self):
#         self.productform.stackedWidget.setCurrentIndex(1)
#     def productNumber(self):
#         self.productform.stackedWidget.setCurrentIndex(2)
#     def sonuc(self):
#         self.sonucform.show()
#         self.hide()
  
            