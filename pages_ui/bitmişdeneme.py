
from PyQt5 import QtCore, QtWidgets


class Ui_product(object):
   
    def setupUi(self, product, urun_listesi):
        product.setObjectName("product")
        product.resize(606, 300)
        self.stackedWidget = QtWidgets.QStackedWidget(product)
        self.stackedWidget.setGeometry(QtCore.QRect(120, 70, 321, 131))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")

        # Product type page---------------------------------------------------------------------------------------
        self.page_product_type = QtWidgets.QWidget()
        self.page_product_type.setObjectName("page_product_type")
        self.h_layout = QtWidgets.QHBoxLayout(self.page_product_type)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(10)

        # Create QPushButton for each product in the product list and add it to the layout
        for urun in urun_listesi:
            button = QtWidgets.QPushButton(urun)
            button.setObjectName(urun)
            self.h_layout.addWidget(button)
            print("1.adım  "+button.objectName())
        for button in self.page_product_type.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.on_product_type_button_clicked)

        # Set layout for the product type page and add it to the stacked widget
        self.page_product_type.setLayout(self.h_layout)
        self.stackedWidget.addWidget(self.page_product_type)
        
         # Product color page--------------------------------------------------------------------------------------
        self.page_2_product_color = QtWidgets.QWidget()
        self.page_2_product_color.setObjectName("page_2_product_color")
        self.color_layout = QtWidgets.QVBoxLayout(self.page_2_product_color)
        self.color_layout.setContentsMargins(0, 0, 0, 0)
        self.color_layout.setSpacing(10)

        # Set layout for the product color page and add it to the stacked widget
        self.page_2_product_color.setLayout(self.color_layout)
        self.stackedWidget.addWidget(self.page_2_product_color)
      
        # for urun in urun_listesi:
        #     button = QtWidgets.QPushButton(urun)
        #     button.setObjectName(urun)
        #     self.h_layout.addWidget(button)
        #     print("1.adım  "+button.objectName())
        # for button in self.page_product_type.findChildren(QtWidgets.QPushButton):
        #     button.clicked.connect(self.on_product_type_button_clicked)



        # Product number page************************************************
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
    def on_product_type_button_clicked(self):
        button = self.page_product_type.sender()
        product_name = button.objectName()

        # Clear any existing color buttons from the color page
        for color_button in self.page_2_product_color.findChildren(QtWidgets.QPushButton):
            self.color_layout.removeWidget(color_button)
            color_button.deleteLater()

        # Get the colors for the selected product and create a QPushButton for each color
        colors = self.get_colors_for_product(product_name)
        for color in colors:
            color_button = QtWidgets.QPushButton(color)
            color_button.setObjectName(color)
            self.color_layout.addWidget(color_button)
            print("2.adım  "+color_button.objectName())
        

        # Set the current index of the stacked widget to the color page
        self.stackedWidget.setCurrentIndex(1)
    def get_colors_for_product(self,product_name):
        if product_name == "kalem" :
            return ["Red", "Blue", "Green"]
        elif product_name == "Jeans":
            return ["Black", "Blue", "Gray"]
        elif product_name == "Shoes":
            return ["Brown", "Black", "White"]
        else:
            return []
        

        # Do something with the product name, such as showing the next page for selecting colors
    def retranslateUi(self, product):
        _translate = QtCore.QCoreApplication.translate
        product.setWindowTitle(_translate("product", "Form"))
 

urun_listesi = {
                    "kalem": {"renkler": {"mavi": 3, "siyah": 5, "kırmızı": 4}, "fiyat": None},
                    "defter": {"renkler": {"sarı": 8, "pembe": 10, "yeşil": 9}, "fiyat": None},
                    "kalemlik": {"renkler": {"mor": 6, "turuncu": 7, "beyaz": 8}, "fiyat": None},
                    "bardak": {"renkler": {"şeffaf": 2, "mavi": 3, "kırmızı": 4}, "fiyat": None}
                }
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    product = QtWidgets.QWidget()
    ui = Ui_product()
    ui.setupUi(product,urun_listesi)
    product.show()
    sys.exit(app.exec_())
