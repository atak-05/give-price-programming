
from PyQt5 import QtCore, QtGui, QtWidgets
from.sonuc_ui import Ui_Sonuc_Form
class Ui_product_Product(object):
    def setupUi(self, product, urun_listesi,on_product_type_button_clicked):
        pixmap = QtGui.QPixmap("pages_ui/image/background-2.png")
        palette = product.palette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        product.setPalette(palette)
        product.setObjectName("product")
        product.resize(750, 450)
        product.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:24px;\n"
"}\n"
"QStackedWidget{\n"
"border-radius:15px;\n"
"background:#6495ed;\n"
"}\n"
"\n"
"#product{\n"
"background:url(:/image/icon/background-2.png);\n"
"}\n"
"QPushButton{\n"
"background:#ecc5e9;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:white;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"")
        product.setObjectName("product")
        product.resize(500, 400)
        self.stackedWidget = QtWidgets.QStackedWidget(product)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 480,400))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")
        self.product_name = None
        self.urun_listesi = {}
        self.color_name = None
        self.number_button =None
        self.on_product_type_button_clicked = on_product_type_button_clicked
        self.page_product_type = None
        # ⁡⁢⁢⁢Product type page---------------------------------------------------------------------------------------⁡
        self.page_product_type = QtWidgets.QWidget()
        self.page_product_type.setObjectName("page_product_type")
        self.h_layout = QtWidgets.QVBoxLayout(self.page_product_type)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(2)
        #Product type Label
        self.label = QtWidgets.QLabel(self.page_product_type)
        self.label.setText("Please choose the type of product")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFixedHeight(40)
        self.h_layout.addWidget(self.label)

        # Create QPushButton for each product in the product list and add it to the layout
        for urun in urun_listesi:
            button = QtWidgets.QPushButton(urun)
            button.setObjectName(urun)
            self.h_layout.addWidget(button)
            print("1.adım  "+button.objectName())
        for button in self.page_product_type.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(on_product_type_button_clicked)
        # Set layout for the product type page and add it to the stacked widget
        self.page_product_type.setLayout(self.h_layout)
        self.stackedWidget.addWidget(self.page_product_type)
        
         # ⁡⁢⁢⁢Product color page--------------------------------------------------------------------------------------⁡
        self.page_2_product_color = QtWidgets.QWidget()
        self.page_2_product_color.setObjectName("page_2_product_color")
        self.color_layout = QtWidgets.QVBoxLayout(self.page_2_product_color)
        for button in self.page_2_product_color.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.on_product_color_button_clicked)

        self.color_layout.setContentsMargins(0, 0, 0, 0)
        self.color_layout.setSpacing(2)

        # Set layout for the product color page and add it to the stacked widget
        self.page_2_product_color.setLayout(self.color_layout)
        self.stackedWidget.addWidget(self.page_2_product_color)

        # Product Number Page---------------------------------------------------------------------------------------⁡
        self.page_3_product_number = QtWidgets.QWidget()
        self.page_3_product_number.setObjectName("page_3_product_number")
        self.number_layout = QtWidgets.QVBoxLayout()
        for button in self.page_3_product_number.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.on_product_color_button_clicked)
            
        self.number_layout.setContentsMargins(0, 0, 0, 0)
        self.number_layout.setSpacing(2)

        # Set layout for the product color page and add it to the stacked widget
        self.page_3_product_number.setLayout(self.number_layout)
        self.stackedWidget.addWidget(self.page_3_product_number)
        
        
     

        # Connect signals and slots
        # self.retranslateUi(product)
        QtCore.QMetaObject.connectSlotsByName(product)
        
        
    
    
    
        # Do something with the product name, such as showing the next page for selecting colors
    def retranslateUi(self, product):
        _translate = QtCore.QCoreApplication.translate
        product.setWindowTitle(_translate("product", "Form"))
 
# urun_adedi = [1,5,10,20,50,100]
urun_listesi = {}
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    product = QtWidgets.QWidget()
    ui = Ui_product_Product()
    ui.setupUi(product,urun_listesi)
    product.show()
    sys.exit(app.exec_())
