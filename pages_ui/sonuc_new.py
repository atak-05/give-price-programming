# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sonuc_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Sonuc(object):
    def setupUi(self, Form):
        pixmap = QtGui.QPixmap("pages_ui/image/background-2.png")
        palette = Form.palette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(pixmap))
        Form.setPalette(palette)
        Form.setObjectName("Form")
        Form.resize(750, 450)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        Form.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"font-size:10px;\n"
"\n"
"}\n"
"#label_text{\n"
"font-size:13px;\n"
"background-color: transparent;\n"
"}\n"
"#label_bilgi{\n"
"font-size:25px;\n"
"color:white;\n"
"}\n"
"#label_sonuc{\n"
"font-size:25px;\n"
"font-weight: bold;\n"
"color:white;\n"
"}\n"
"QFrame{\n"
"border-radius:15px;\n"
"background:#6495ed;\n"
"}\n"
"\n"
"#Form{\n"
"background:url(:/image/icon/background-2.png);\n"
"}\n"
"QPushButton{\n"
"background:transparent;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color:#black;\n"
"border-radius:15px;\n"
"background:white;\n"
"}\n"
"\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(200, 100, 350, 250))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_sonuc = QtWidgets.QLabel(self.frame)
        self.label_sonuc.setGeometry(QtCore.QRect(90, 70, 191, 61))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_sonuc.setFont(font)
        self.label_sonuc.setObjectName("label_sonuc")
        self.label_bilgi = QtWidgets.QLabel(self.frame)
        self.label_bilgi.setGeometry(QtCore.QRect(160, 130, 200, 61))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.label_bilgi.setFont(font)
        self.label_bilgi.setObjectName("label_bilgi")
        self.button_home = QtWidgets.QPushButton("<-- Anasayfaya dön",Form)
        self.button_home.setGeometry(QtCore.QRect(300, 350, 311, 31))
        self.button_home.setFixedSize(150,50)
        self.button_home.setObjectName("button_home")
        self.label_text = QtWidgets.QLabel(Form)
        self.label_text.setGeometry(QtCore.QRect(230, 390, 311, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setUnderline(True)
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")
        
        
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_sonuc.setText(_translate("Form", "TOPLAM FİYAT"))
        self.label_bilgi.setText(_translate("Form", ""))
        #ContactFormPage will added in here!!!
        self.label_text.setText(_translate("Form", "LÜtfen daha detaylı bilgi için bizimle iletişime geçin."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Sonuc()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
