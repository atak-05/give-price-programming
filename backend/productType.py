from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QStackedWidget

class ProductTypes(QWidget):
    def __init__(self):
        super().__init__()

        # Ürün tiplerini ve butonu oluşturun
        self.product_types = QListWidget()
        self.product_types.addItems(['KALEM', 'KAĞIT', 'DEFTER'])
        self.select_button = QPushButton('Seç')

        # Ürün tipleri ve butonu için düzenleyicileri ayarlayın
        self.product_layout = QVBoxLayout()
        self.product_layout.addWidget(self.product_types)
        self.product_layout.addWidget(self.select_button)

        # Ürün tipleri için widget'ı oluşturun ve düzenleyiciyi ayarlayın
        self.product_widget = QWidget()
        self.product_widget.setLayout(self.product_layout)

        # Ana düzenleyiciyi oluşturun ve ürün widget'ını ekleyin
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('Ürün Tipini Seçin:'))
        self.layout.addWidget(self.product_widget)

        # Widget'ı ayarlayın
        self.setLayout(self.layout)

        # Seç butonunu tıklayınca ürün detay sayfasına geçin
        self.select_button.clicked.connect(self.show_product_detail)

    def show_product_detail(self):
        # Seçilen ürünü alın
        selected_item = self.product_types.currentItem().text()

        # Yeni sayfayı oluşturun
        product_detail = ProductDetail(selected_item)

        # Ana widget'ı bulun ve QStackedWidget'ı elde edin
        main_window = self.window()
        stacked_widget = main_window.findChild(QStackedWidget)

        # Yeni sayfayı QStackedWidget'a ekleyin
        stacked_widget.addWidget(product_detail)

        # Yeni sayfayı gösterin
        stacked_widget.setCurrentWidget(product_detail)
