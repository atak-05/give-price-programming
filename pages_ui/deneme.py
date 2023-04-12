
from PyQt5 import QtCore, QtWidgets


class Ui_product(object):
   
    def setupUi(self, product, urun_listesi):
        
        product.setObjectName("product")
        product.resize(500, 400)
        self.stackedWidget = QtWidgets.QStackedWidget(product)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 480,400))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")
        self.product_name = None
        self.color_name = None
        # ⁡⁢⁢⁢Product type page---------------------------------------------------------------------------------------⁡
        self.page_product_type = QtWidgets.QWidget()
        self.page_product_type.setObjectName("page_product_type")
        self.h_layout = QtWidgets.QHBoxLayout(self.page_product_type)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setSpacing(2)

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
      
        # for urun in urun_listesi:
        #     button = QtWidgets.QPushButton(urun)
        #     button.setObjectName(urun)
        #     self.h_layout.addWidget(button)
        #     print("1.adım  "+button.objectName())
        # for button in self.page_product_type.findChildren(QtWidgets.QPushButton):
        #     button.clicked.connect(self.on_product_type_button_clicked)



        # ⁡⁣⁣⁢Product number page************************************************⁡
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
    def on_product_type_button_clicked(self):
        button = self.page_product_type.sender()
        self.product_name = button.objectName()

        # Clear any existing color buttons from the color page
        for color_button in self.page_2_product_color.findChildren(QtWidgets.QPushButton):
            self.color_layout.removeWidget(color_button)
            color_button.deleteLater()
        # Clear any existing number buttons from the number page
        for number_button in self.page_3_product_number.findChildren(QtWidgets.QPushButton):
            self.number_layout.removeWidget(number_button)
            number_button.deleteLater()
            
          
        
        # Get the colors for the selected product and create a QPushButton for each color
        colors = self.get_colors_for_product(self.product_name)
        for color in colors:
            color_button = QtWidgets.QPushButton(color)
            color_button.setObjectName(color)
            self.color_layout.addWidget(color_button)
            print("2.adım  "+color_button.objectName())
            color_button.clicked.connect(lambda checked, color_name=color: self.on_product_color_button_clicked(color_name))

        
        
        
        self.button2 = QtWidgets.QPushButton("<-- geri", self.page_2_product_color)
        # self.button2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.button2.setFixedSize(70,30)
        self.color_layout.addWidget(self.button2)
        self.button2.clicked.connect(self.go_back)
        
         # Create a horizontal layout for the color and back buttons
        self.color_button_layout = QtWidgets.QHBoxLayout()
        self.color_button_layout.addWidget(self.button2)
        # Add the color buttons and the horizontal layout to the color layout
        self.color_layout.addLayout(self.color_button_layout)
        
        self.stackedWidget.setCurrentIndex(1)
        
    #​‌‍‌⁡⁣⁣⁢Çalışılıyorr.................    
    # 
    # ⁡​
    def on_product_color_button_clicked(self,color_name):
           
        
        for i in reversed(range(self.number_layout.count())):
            widgetToRemove = self.number_layout.itemAt(i).widget()
            if widgetToRemove is not None:
                widgetToRemove.setParent(None)
        button = self.page_2_product_color.sender()
        self.color_name = button.objectName()
        product_name = self.product_name
        print("3.adım da product: " + product_name)
        print("3.adım buton adı " +self.color_name)
        
        numbers = self.get_number_for_product(product_name)
        for number in numbers:
            number_button = QtWidgets.QPushButton(str(number))
            number_button.setObjectName(str(number))
            number_button.setMinimumWidth(100)
            self.number_layout.addWidget(number_button)
            print("3.adım  "+number_button.objectName())
        self.button2 = QtWidgets.QPushButton("<-- geri", self.page_2_product_color)
        self.button2.setFixedSize(70,30)
        self.button2.clicked.connect(self.go_back)
        self.number_layout.addWidget(self.button2)     
        self.button2.clicked.connect(self.go_back)

       

        
        # self.button2 = QtWidgets.QPushButton("<-- geri", self.page_2_product_color)
        # # self.button2.setGeometry(QtCore.QRect(10, 10, 75, 23))
        # self.button2.setFixedSize(70,30)
        # self.number_layout.addWidget(self.button2)
        # self.button2.clicked.connect(self.go_back)
            
        
         # Create a horizontal layout for the color and back buttons
        self.number_button_layout = QtWidgets.QHBoxLayout()
        self.number_button_layout.addWidget(self.button2)
        # Add the color buttons and the horizontal layout to the color layout
        self.number_layout.addLayout(self.number_button_layout)
        
        self.stackedWidget.setCurrentIndex(2)
        
        # color_name = button.objectName()
        # product_name = button.objectName()
        # # Clear any existing number buttons from the number page
        # for number_button in self.page_3_product_number.findChildren(QtWidgets.QPushButton):
        #     self.number_layout.removeWidget(number_button)
        #     number_button.deleteLater()

        # # Get the numbers for the selected product and color, and create a QPushButton for each number
        # numbers = self.get_numbers_for_product_color(product_name, color_name)
        # for number in numbers:
        #     number_button = QtWidgets.QPushButton(str(number))
        #     number_button.setObjectName(str(number))
        #     self.number_layout.addWidget(number_button)
        #     print("3.adım  "+number_button.objectName())

        # self.button3 = QtWidgets.QPushButton("<-- geri", self.page_3_product_number)
        # self.button3.setFixedSize(70,30)
        # self.number_layout.addWidget(self.button3)
        # self.button3.clicked.connect(self.go_back)
        # self.stackedWidget.setCurrentIndex(2)

            
            
            
     #​‌‍‌⁡⁢⁢⁡⁣⁣⁢...............................................⁡  ⁡​ 
    def go_back(self):
        # Get the current index of the stacked widget
        current_index = self.stackedWidget.currentIndex()
        
        # If the current index is 0, there is no page to go back to
        self.stackedWidget.setCurrentIndex(current_index - 1)
        self.number_layout.removeWidget(self.button2)
        
        
    def get_colors_for_product(self,product_name):
        color =[]
        for urun in urun_listesi:
            print(product_name)
            print(urun)
            if product_name == urun:
                for renk in urun_listesi[urun]['renkler'].keys():
                    color.append(renk)
                return color
            else:
                 continue

    def get_number_for_product(self,product_name):
        number=[]
        for urun in urun_listesi:
            print(product_name)
            print(urun)
            if product_name == urun:
                for renk in urun_listesi[urun]['adet']:
                    number.append(renk)
                return number
            else:
                 continue
        # Do something with the product name, such as showing the next page for selecting colors
    def retranslateUi(self, product):
        _translate = QtCore.QCoreApplication.translate
        product.setWindowTitle(_translate("product", "Form"))
 
urun_adedi = [1,5,10,20,50,100]
urun_listesi = {
                    "kalem": {"renkler": {"mavi": 3, "siyah": 5, "kırmızı": 4}, "fiyat": None,"adet":{1,5,10,20,50,100}},
                    "defter": {"renkler": {"sarı": 8, "pembe": 10, "yeşil": 9}, "fiyat": None,"adet":{1,5,10,20,50,100}},
                    "kalemlik": {"renkler": {"mor": 6, "turuncu": 7, "beyaz": 8}, "fiyat": None,"adet":{1,5,10,20,50,100}},
                    "bardak": {"renkler": {"şeffaf": 2, "mavi": 3, "kırmızı": 4}, "fiyat": None,"adet":{1,5,10,20,50,100}}
                }
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    product = QtWidgets.QWidget()
    ui = Ui_product()
    ui.setupUi(product,urun_listesi)
    product.show()
    sys.exit(app.exec_())
