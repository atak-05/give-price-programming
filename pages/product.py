from PyQt5.QtWidgets import *
from pages_ui.product_python import Ui_product
from pages_ui.product_new import Ui_product_Product
from pages_ui.sonuc_ui import Ui_Sonuc_Form
from .sonuc import SonucPage
# from pages_ui.product_python import Ui_product
from PyQt5 import QtCore, QtWidgets


class ProductPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.urun_listesi = {
                    "kalem": {"renkler": {"mavi": 3, "siyah": 5, "kırmızı": 4}, "fiyat": None,"adet":{1,5,10,20,50,100}},
                    "defter": {"renkler": {"sarı": 8, "pembe": 10, "yeşil": 9}, "fiyat": None,"adet":{1,5,10,20,50,100}},
                    "kalemlik": {"renkler": {"mor": 6, "turuncu": 7, "beyaz": 8}, "fiyat": None,"adet":{1,5,10,20,50,100}},
                    "bardak": {"renkler": {"şeffaf": 2, "mavi": 3, "kırmızı": 4}, "fiyat": None,"adet":{1,5,10,20,50,100}}
                }
        self.sonuc_page =SonucPage()
        self.productform = Ui_product_Product()
        self.productform.setupUi(self,self.urun_listesi,self.on_product_type_button_clicked)
        self.sonuc_ui = Ui_Sonuc_Form()
        
        self.number_name= self.productform.number_button
        self.productform.on_product_type_button_clicked= self.on_product_type_button_clicked
    #===========================================================================================#    
    #===========================================================================================#      
    def on_product_type_button_clicked(self):
        button =self.productform.page_product_type.sender()
        self.product_name = button.objectName()
        for color_button in self.productform.page_2_product_color.findChildren(QtWidgets.QPushButton):
            self.productform.color_layout.removeWidget(color_button)
            color_button.deleteLater()
        # Clear any existing number buttons from the number page
        for number_button in self.productform.page_3_product_number.findChildren(QtWidgets.QPushButton):
            self.productform.number_layout.removeWidget(number_button)
            number_button.deleteLater()
        
        colors =self.get_colors_for_product(self.product_name)
        #! You can find label of product type where product_python.py
        # Add a label to the color page
        self.label = QtWidgets.QLabel(self.productform.page_2_product_color)
        self.label.setText("Please choose the color of product")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFixedHeight(40)
        self.productform.color_layout.addWidget(self.label)
        
        for color in colors:
            color_button = QtWidgets.QPushButton(color)
            color_button.setObjectName(color)
            self.productform.color_layout.addWidget(color_button)
            print("2.adım  "+color_button.objectName())
            color_button.clicked.connect(lambda checked, color_name=color: self.on_product_color_button_clicked(color_name))
       
        
        
        
        self.button2 = QtWidgets.QPushButton("<-- geri", self.productform.page_2_product_color)
        # self.button2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.button2.setFixedSize(70,30)
        self.productform.color_layout.addWidget(self.button2)
        self.button2.clicked.connect(self.go_back)
        
         # Create a horizontal layout for the color and back buttons
        color_button_layout = QtWidgets.QHBoxLayout()
        color_button_layout.addWidget(self.button2)
        # Add the color buttons and the horizontal layout to the color layout
        self.productform.color_layout.addLayout(color_button_layout)
        
        self.productform.stackedWidget.setCurrentIndex(1)
       
        
    #===========================================================================================#        
    def get_colors_for_product(self,product_name):
        color =[]
        for urun in self.urun_listesi:
            print(self.product_name)
            print(urun)
            if self.product_name == urun:
                for renk in self.urun_listesi[urun]['renkler'].keys():
                    color.append(renk)
                return color
            else:
                continue
    def go_back(self):
        self.current_index = self.productform.stackedWidget.currentIndex()
        self.productform.stackedWidget.setCurrentIndex(self.current_index-1)
    #===========================================================================================#      
    #===========================================================================================#                
    def on_product_color_button_clicked(self,number_button=None):
        for i in reversed(range(self.productform.number_layout.count())):
            widgetToRemove = self.productform.number_layout.itemAt(i).widget()
            if widgetToRemove is not None:
                widgetToRemove.setParent(None)
        button = self.productform.page_2_product_color.sender()
        self.color_name = button.objectName()
        self.product_name = self.product_name
        print("3.adım da product: " + self.product_name)
        print("3.adım buton adı " +self.color_name)
        
         # Add a label to the number page
        self.label = QtWidgets.QLabel(self.productform.page_3_product_number)
        self.label.setText("Please choose the number of product")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFixedHeight(40)
        self.productform.number_layout.addWidget(self.label)
        
        numbers = self.get_number_for_product(self.product_name)
        for number in numbers:
            self.number_button = QtWidgets.QPushButton(str(number))
            self.number_button.setObjectName(str(number))
            self.number_button.setMinimumWidth(100)
            self.productform.number_layout.addWidget(self.number_button)
            print("3.adım  "+self.number_button.objectName())
            self.number_button.clicked.connect(lambda checked, number_name=number: self.on_number_button_clicked(number_name))

        self.button2 = QtWidgets.QPushButton("<-- geri", self.productform.page_2_product_color)
        self.button2.setFixedSize(70,30)
        self.button2.clicked.connect(self.go_back)
        self.productform.number_layout.addWidget(self.button2)     
        
        # Create a horizontal layout for the color and back buttons
        self.number_button_layout = QtWidgets.QHBoxLayout()
        self.number_button_layout.addWidget(self.button2)
        # Add the color buttons and the horizontal layout to the color layout
        self.productform.number_layout.addLayout(self.number_button_layout)
        self.productform.stackedWidget.setCurrentIndex(2)
    #===========================================================================================#        
    def get_number_for_product(self,product_name):
        number=[]
        for urun in self.urun_listesi:
            print(self.product_name)
            print(urun)
            if self.product_name == urun:
                for renk in self.urun_listesi[urun]['adet']:
                    number.append(renk)
                return number
            else:
                 continue
             
             
    #===========================================================================================#
    def on_number_button_clicked(self,number_name=None):
        number_button = self.productform.page_3_product_number.sender()
        self.number_name = number_button.objectName()
        self.number_name = int(self.number_name)
        print(self.number_name)
        self.result_price(self.color_name,self.product_name,self.number_name)
    #===========================================================================================#
    def result_price(self,color_name,product_name,number):
        
        self.color_name=color_name
        self.product_name = product_name
        self.number = int(number)
       
        product_price = int(self.urun_listesi[self.product_name]['renkler'][self.color_name])
        
        self.total_price = int(product_price*number)
        print(product_price)
        print(self.total_price)
        self.result_page()

    def result_page(self):
        self.close()
        total = str(self.total_price)
        self.sonuc_page.sonuc.label_bilgi.setText(total)
        self.sonuc_page.show()
      