from PyQt5.QtWidgets import *
from pages_ui.product_python import Ui_product
from .product import Ui_product


class ProductPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_product()
        self.loginform.setupUi(self)
        