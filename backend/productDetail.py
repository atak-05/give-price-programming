from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class ProductDetail(QWidget):
    def __init__(self, item_name, colors, prices, parent=None):
        super().__init__(parent)

        # Create a label to show the selected item
        self.item_label = QLabel(item_name, self)
        self.item_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")

        # Create a label to show the available colors
        self.color_label = QLabel("Available colors:", self)
        self.color_label.setStyleSheet("font-size: 16px; margin-bottom: 5px;")

        # Create a vertical layout to add the labels and color checkboxes
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.item_label)
        self.layout.addWidget(self.color_label)

        # Create checkboxes for each color option
        for color in colors:
            checkbox = QCheckBox(color, self)
            checkbox.setChecked(False)
            self.layout.addWidget(checkbox)

        # Create a label to show the available prices
        self.price_label = QLabel("Available prices:", self)
        self.price_label.setStyleSheet("font-size: 16px; margin-top: 10px; margin-bottom: 5px;")
        self.layout.addWidget(self.price_label)

        # Create a label for each price option
        for price in prices:
            price_label = QLabel(price, self)
            price_label.setStyleSheet("margin-bottom: 3px;")
            self.layout.addWidget(price_label)

        # Set the layout for the widget
        self.setLayout(self.layout)
