import sys
import platform
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

class Ui_ViewPush(object):
    def setupUi(self, ViewPush):
        if not ViewPush.objectName():
            ViewPush.setObjectName(u"ViewPush")
        ViewPush.resize(337, 250)
        ViewPush.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        ViewPush.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(ViewPush)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(50,50,50,1);\n"
"	rgb: (170, 0, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_tituloPush = QLabel(self.dropShadowFrame)
        self.label_tituloPush.setObjectName(u"label_tituloPush")
        self.label_tituloPush.setGeometry(QRect(0, 20, 321, 61))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        self.label_tituloPush.setFont(font)
        self.label_tituloPush.setStyleSheet(u"color: rgba(248, 255, 36, 0.97);")
        self.label_tituloPush.setAlignment(Qt.AlignCenter)
        self.label_descricaoPush = QLabel(self.dropShadowFrame)
        self.label_descricaoPush.setObjectName(u"label_descricaoPush")
        self.label_descricaoPush.setGeometry(QRect(12, 110,300, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_descricaoPush.setFont(font1)
        self.label_descricaoPush.setStyleSheet(u"color: rgb(255,255,255);")
        self.label_descricaoPush.setAlignment(Qt.AlignCenter)
        self.btn_okPush = QPushButton(self.dropShadowFrame)
        self.btn_okPush.setObjectName(u"btn_okPush")
        self.btn_okPush.setGeometry(QRect(89, 170, 141, 51))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_okPush.setFont(font2)
        self.btn_okPush.setStyleSheet(u"QPushButton#btn_okPush{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(187, 187, 186,1), stop: 1 rgba(150, 150, 150, 255));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton#btn_okPush:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(150, 150, 150, 255), stop: 1 rgba(187, 187, 186,1));\n"
"}\n"
"QPushButton#btn_okPush:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgba(232, 49, 49, 255);\n"
"}")

        self.verticalLayout.addWidget(self.dropShadowFrame)

        ViewPush.setCentralWidget(self.centralwidget)
        


        self.retranslateUi(ViewPush)

        QMetaObject.connectSlotsByName(ViewPush)
    
    def fecharTela(self):
        sys.exit()
        
        
    # setupUi

    def retranslateUi(self, ViewPush):
        ViewPush.setWindowTitle(QCoreApplication.translate("ViewPush", u"Aviso!", None))
        self.label_tituloPush.setText(QCoreApplication.translate("ViewPush", u"<strong>Aviso!</strong>", None))
        self.btn_okPush.setText(QCoreApplication.translate("ViewPush", u"Ok", None))
    # retranslateUi

