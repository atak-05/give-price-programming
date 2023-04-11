from PyQt5.QtWidgets import *
from pages_ui.product_python import Ui_product
from .sonuc import SonucPage


class ProductPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.productform = Ui_product()
        self.productform.setupUi(self)
        self.productform.pushButton_product_type.clicked.connect(self.productColor)
        self.productform.pushButton_2_product_color.clicked.connect(self.productNumber)
        self.productform.pushButton_3_product_number.clicked.connect(self.sonuc)
        self.sonucform = SonucPage()
        
    def productColor(self):
        self.productform.stackedWidget.setCurrentIndex(1)
    def productNumber(self):
        self.productform.stackedWidget.setCurrentIndex(2)
    def sonuc(self):
        self.sonucform.show()
        self.hide()
        
            