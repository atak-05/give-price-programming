from PyQt5.QtWidgets import QApplication

from productColor1 import productColor
app = QApplication([])

pencere = productColor()
pencere.show()
app.exec_()
