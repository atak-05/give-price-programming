from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout,QDialog

class MyPage(QDialog):
    def __init__(self):
        super(MyPage,self).__init__()
        
        # QLabel nesnesi oluştur
        label = QLabel("Bu bir örnek sayfadır.")
        
        # QVBoxLayout nesnesi oluştur
        layout = QVBoxLayout()
        
        # QLabel nesnesini layout'a ekle
        layout.addWidget(label)
        
        # Widget'a layout'u ekle
        self.setLayout(layout)
