
from PyQt5 import QtCore, QtWidgets


class Ui_product(object):
    def setupUi(self, product, urun_listesi):
        product.setObjectName("product")
        product.resize(606, 300)
        self.stackedWidget = QtWidgets.QStackedWidget(product)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 70, 321, 131))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")

        # Product type page
        self.page_product_type = QtWidgets.QWidget()
        self.page_product_type.setObjectName("page_product_type")
        h_layout = QtWidgets.QHBoxLayout(self.page_product_type)
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setSpacing(10)

        # Create QPushButton for each product in the product list and add it to the layout
        for urun in urun_listesi:
            button = QtWidgets.QPushButton(urun)
            button.setObjectName(urun)
            h_layout.addWidget(button)

        # Set layout for the product type page and add it to the stacked widget
        self.page_product_type.setLayout(h_layout)
        self.stackedWidget.addWidget(self.page_product_type)

        # Product color page
        self.page_2_product_color = QtWidgets.QWidget()
        self.page_2_product_color.setObjectName("page_2_product_color")
        self.pushButton_2_product_color = QtWidgets.QPushButton(self.page_2_product_color)
        self.pushButton_2_product_color.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_2_product_color.setObjectName("pushButton_2_product_color")
        self.stackedWidget.addWidget(self.page_2_product_color)

        # Product number page
        self.page_3_product_number = QtWidgets.QWidget()
        self.page_3_product_number.setObjectName("page_3_product_number")
        self.pushButton_3_product_number = QtWidgets.QPushButton(self.page_3_product_number)
        self.pushButton_3_product_number.setGeometry(QtCore.QRect(120, 60, 75, 23))
        self.pushButton_3_product_number.setObjectName("pushButton_3_product_number")
        self.stackedWidget.addWidget(self.page_3_product_number)

        # Set the initial stacked widget index to the product type page
        self.stackedWidget.setCurrentIndex(0)

        # Connect signals and slots
        # self.retranslateUi(product)
        QtCore.QMetaObject.connectSlotsByName(product)

    def retranslateUi(self, product):
        _translate = QtCore.QCoreApplication.translate
        product.setWindowTitle(_translate("product", "Form"))
        self.pushButton_product_type.setText(_translate("product", "ürün type"))
        self.pushButton_2_product_color.setText(_translate("product", "ürün rengi"))
        self.pushButton_3_product_number.setText(_translate("product", "ürün adedi"))

urun_listesi = { }
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    product = QtWidgets.QWidget()
    ui = Ui_product()
    ui.setupUi(product,urun_listesi)
    product.show()
    sys.exit(app.exec_())
